\# SDN Learning Switch Controller (Mininet + POX)



\## 📌 Problem Statement



Implement an SDN controller that mimics a learning switch by dynamically learning MAC addresses and installing forwarding rules.



\---



\## ⚙️ Tools Used



\* Mininet

\* POX Controller

\* Open vSwitch

\* Ubuntu 24.04



\---



\## 🧠 Concept



A learning switch dynamically learns MAC addresses and maps them to switch ports. Initially, packets are flooded. Once MAC addresses are learned, flow rules are installed for direct forwarding.



\---



\## 🛠️ Setup Steps



\### 1. Install Mininet



sudo apt update

sudo apt install mininet -y



\### 2. Clone POX



git clone https://github.com/noxrepo/pox.git

cd pox



\### 3. Run Controller



./pox.py forwarding.l2\_learning



\### 4. Start Mininet



sudo mn --controller=remote --topo=single,3



\---



\## 🧪 Execution Steps



\### Test Connectivity



pingall



\### Flow Table Inspection



sudo ovs-ofctl -O OpenFlow10 dump-flows s1



\---



\## 📊 Results



\* Successful packet forwarding (0% packet loss)

\* Dynamic MAC learning

\* Flow rules installed in switch

\* Controller-switch communication established



\---



\## 🧪 Test Scenarios



\### Scenario 1: Normal Operation



\* pingall successful



\### Scenario 2: Failure Case



\* link s1 h2 down → communication fails

\* link restored → communication resumes



\---



\## 📸 Proof of Execution



\### Ping Results



!\[Ping](screenshots/4\_pingall.png)



\### Flow Table



!\[Flow](screenshots/5\_flow\_table.png)



\### Failure Scenario



!\[Failure](screenshots/6\_failure\_test.png)



\---



\## 📚 References



\* https://mininet.org/

\* https://github.com/noxrepo/pox



