from conftest import CONTRACT
def test_mapping_and_window(direct_vm,direct_deploy,direct_alice,direct_bob):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT);x.request_mapping('ct-1','0x'+direct_bob.hex(),'Distributed Systems','https://home.example/s','https://target.example/s',['consensus','fault tolerance']);direct_vm.sender=direct_bob;direct_vm.mock_web(r'.*\.example',{'status':200,'body':'Consensus and fault-tolerance syllabus.'});direct_vm.mock_llm(r'.*CurriculumThread equivalence map.*','{"matched_indexes":[0,1],"missing_indexes":[],"prerequisites":[]}');x.map_outcomes('ct-1');assert x.get_thread('ct-1')['state']=='MAPPED';direct_vm.sender=direct_alice;x.object_mapping('ct-1','https://appeal.example/proof');assert x.get_thread('ct-1')['state']=='OBJECTED'
def test_institution_only(direct_vm,direct_deploy,direct_alice,direct_bob):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT);x.request_mapping('ct-1','0x'+direct_bob.hex(),'Distributed Systems','https://home.example/s','https://target.example/s',['consensus','fault tolerance'])
 with direct_vm.expect_revert('receiving institution'):x.map_outcomes('ct-1')
