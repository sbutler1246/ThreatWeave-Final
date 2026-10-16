r"""Check ThreatWeave's Neo4j and Ollama connections without changing data.

Run with the project environment: .venv\Scripts\python.exe check_connections.py
"""

import argparse
import getpass
import sys


def prompt(label, default):
    return input(f"{label} [{default}]: ").strip() or default


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uri", help="Neo4j connection URI")
    parser.add_argument("--user", help="Neo4j username")
    parser.add_argument("--database", help="Database name within the instance")
    parser.add_argument("--ollama-url", default="http://localhost:11434")
    parser.add_argument("--model", default="llama3.1:8b")
    args = parser.parse_args()

    try:
        import requests
        from neo4j import GraphDatabase, Query
        from neo4j.exceptions import AuthError
    except ImportError as error:
        print(f"FAIL: A required Python package is missing: {error.name}.")
        print("Run this file using ThreatWeave's .venv\\Scripts\\python.exe.")
        return 1

    print("ThreatWeave connection check")
    print(f"Python: {sys.version.split()[0]}")
    print("Use the connection details from the ThreatWeave instance in Neo4j Desktop.")
    uri = args.uri or prompt("Neo4j URI", "bolt://localhost:7687")
    user = args.user or prompt("Neo4j username", "neo4j")
    database = args.database or prompt("Database name (not the instance name)", "neo4j")
    password = getpass.getpass("Neo4j password (typing is hidden): ")
    ok = True

    try:
        with GraphDatabase.driver(
            uri,
            auth=(user, password),
            connection_timeout=10,
            connection_acquisition_timeout=15,
        ) as driver:
            driver.verify_connectivity()
            with driver.session(database=database, default_access_mode="READ") as session:
                session.run(Query("RETURN 1 AS connected", timeout=15)).consume()
                print(f"PASS: Neo4j connection and database access ({database}).")

                expected = {
                    "entity_id_unique", "doc_id_unique",
                    "chunk_id_unique", "assertion_id_unique",
                }
                actual = {
                    row["name"] for row in session.run(
                        Query("SHOW CONSTRAINTS YIELD name RETURN name", timeout=15)
                    )
                }
                missing = sorted(expected - actual)
                if missing:
                    print("FAIL: Missing ThreatWeave constraints: " + ", ".join(missing))
                    print("Check that you selected the database where you created the schema.")
                    ok = False
                else:
                    print("PASS: All four ThreatWeave constraints are present.")
    except AuthError:
        print("FAIL: Neo4j login was rejected. Check the instance's username and password.")
        ok = False
    except Exception as error:
        detail = str(error)
        if password:
            detail = detail.replace(password, "[hidden]")
        print(f"FAIL: Neo4j connection check: {type(error).__name__}: {detail}")
        ok = False
    finally:
        password = None

    try:
        response = requests.get(args.ollama_url.rstrip("/") + "/api/tags", timeout=(5, 15))
        response.raise_for_status()
        models = response.json().get("models", [])
        model = next((entry for entry in models if entry.get("name") == args.model), None)
        if model is None:
            print(f"FAIL: Ollama is reachable, but {args.model} was not listed.")
            print(f"Install it with: ollama pull {args.model}")
            ok = False
        else:
            print(f"PASS: Ollama API is reachable and {args.model} is installed.")
            if model.get("digest"):
                print("Model digest: " + model["digest"])
    except (requests.RequestException, ValueError, TypeError, AttributeError) as error:
        print(f"FAIL: Ollama API check: {type(error).__name__}: {error}")
        print("Open Ollama and check the API address (default: http://localhost:11434).")
        ok = False

    print()
    print("READY: Both connections and the schema check passed." if ok
          else "NOT READY: Resolve the FAIL messages above, then run this check again.")
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nConnection check cancelled.")
        sys.exit(2)
