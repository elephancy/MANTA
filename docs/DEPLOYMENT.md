# Production releases

The private deployment controller discovers MANTA's exact `main` commit after
both `MANTA CI Android` and `MANTA CI Python` succeed. It owns the approved build
contract, immutable image publication, runtime configuration, health checks,
backups, and rollback. Android, Python, and website CI remain in this repository.

This repository has no production publisher workflow, registry identity, shared
release caller, deployment manifest, or deployment credentials. Application
changes must retain the required CI gates; deployment policy changes belong in
the private controller. Runtime secrets remain in the controller-managed runtime.

Run `python tools/check_deployment_boundary.py` to verify this boundary. A passing
application build is CI evidence; production success is established separately
by the controller's signed deployment receipt.
