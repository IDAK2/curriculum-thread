from pathlib import Path
T=Path('contracts/contract.py').read_text();P=Path('docs/index.html').read_text()
def test_surface():
 for n in ('request_mapping','map_outcomes','object_mapping','finalize','get_thread'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="loom"' in P and 'id="outcomeRail"' in P
