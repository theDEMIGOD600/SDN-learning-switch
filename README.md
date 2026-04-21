SDN Learning Switch Controller (Mininet + POX)



Problem Statement
Implement an SDN controller that mimics a learning switch by dynamically learning MAC addresses and installing forwarding rules.

Tools Used
-Mininet
-POX Controller
-Open vSwitch
-Ubuntu 24.04



A learning switch dynamically learns MAC addresses and maps them to switch ports. Initially, packets are flooded. Once MAC addresses are learned, flow rules are installed for direct forwarding.


Setup Steps
1. Install Mininet

sudo apt update

sudo apt install mininet -y



2.Clone POX

git clone https://github.com/noxrepo/pox.git

cd pox


3. Run Controller

./pox.py forwarding.l2\_learning


4. Start Mininet



sudo mn --controller=remote --topo=single,3



Execution Steps
1. Test Connectivity
pingall

Flow Table Inspection
sudo ovs-ofctl -O OpenFlow10 dump-flows s1


📊 Results

1.Successful packet forwarding (0% packet loss)
2.Dynamic MAC learning
3.Flow rules installed in switch
4. Controller-switch communication established



🧪 Test Scenarios

Scenario 1: Normal Operation
pingall successful


Scenario 2: Failure Case
link s1 h2 down → communication fails
link restored → communication resumes



References
https://mininet.org/
https://github.com/noxrepo/pox



