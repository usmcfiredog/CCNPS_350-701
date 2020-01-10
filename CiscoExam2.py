import random
# from PIL import Image


class QA:
    def __init__(self, question, otherAnswers, correctAnswer,
                 correctAnswer2=None, correctAnswer3=None,
                 correctAnswer4=None, correctAnswer5=None):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAnsw = otherAnswers
        self.corrAnsw2 = correctAnswer2
        self.corrAnsw3 = correctAnswer3
        self.corrAnsw4 = correctAnswer4
        self.corrAnsw5 = correctAnswer5


qaList = [
    QA('A network administrator needs to implement a service that enables granular control of IOS commands that can be executed. Which AAA authentication method should be selected?',
        ['RADIUS', 'Windows Active Directory', 'Generic LDAP'], 'TACACS+'),
    QA('An administrator can leverage which attribute to assign privileges based on Microsoft Active Directory user groups?',
        ['group', 'class', 'person'], 'member of'),
    QA('Cisco 802.1X phasing enables flexible deployments through the use of open, low-impact, and closed modes. What is a unique characteristic of the most secure mode?',
        [
            'Granular ACLs applied prior to authentication',
            'Per user dACLs applied after successful authentication',
            'Adjustable 802.1X timers to enable successful authentication'
        ], 'Only EAPoL traffic allowed prior to authentication'),
    QA('A network administrator must enable which protocol extension to utilize EAP-Chaining?',
        ['EAP-TLS', 'MSCHAPv2', 'PEAP'], 'EAP-FAST'),
    QA('In the command "aaa authentication default group tacacs local", how is the word "default" defined?',
        ['Group name', 'Command Set', 'Login type'], 'Method List'),
    QA('The NAC Agent uses which port and protocol to send discovery packets to an ISE Policy Service Node?',
        ['tcp/8905', 'http/80', 'https/443'], 'udp/8905'),
    QA('Which two conditions are valid when configuring ISE for posturing? (Choose two.)',
        ['Dictionary', 'member of', 'Profile status'],
        'File', 'Service'),
    QA('Which three statements about the given configuration are true? (Choose three.)',
        ['TACACS+ authentication configuration is complete.',
         'TACACS+ server hosts are misconfigured.',
         'The TACACS+ server key is encrypted.'],
        'TACACS+ authentication configuration is incomplete.',
        'TACACS+ server hosts are configured correctly.',
        'The TACACS+ server key is unencrypted.'),
    QA('In AAA, what function does authentication perform?',
        ['It identifies the actions that the user can perform on the device.',
         'It identifies the actions that a user has previously taken.',
         'It identifies what the user can access.'],
        'It identifies the user who is trying to access a device.'),
    QA('Which identity store option allows you to modify the directory services that run on TCP/IP?',
        ['RSA SecurID server', 'RADIUS', 'Active Directory'],
        'Lightweight Directory Access Protocol'),
    QA('Which term describes a software application that seeks connectivity to the network via a network access device?',
        ['authenticator', 'server', 'WLC'], 'supplicant'),
    QA('Cisco ISE distributed deployments support which three features? (Choose three.)',
        ['global implementation of the profiler service in Cisco ISE',
         'server-specific probe configuration', 'NetFlow probes'],
        'global implementation of the profiler service CoA',
        'configuration to send system logs to the appropriate profiler node',
        'node-specific probe configuration'),
    QA('How frequently does the Profiled Endpoints dashlet refresh data?',
        ['every 30 seconds', 'every 2 minutes', 'every 5 minutes'],
        'every 60 seconds'),
    QA('Which command in the My Devices Portal can restore a previously lost device to the network?',
        ['Reset', 'Found', 'Request'], 'Reinstate'),
    QA('What is the first step that occurs when provisioning a wired device in a BYOD scenario?',
        ['The URL redirects to the Cisco ISE Guest Provisioning portal.',
         'Cisco ISE authenticates the user and deploys the SPW package.',
         'The device user attempts to access a network URL.'],
        'The smart hub detects that the physically connected endpoint requires configuration and must use MAB to authenticate.'),
    QA('Which three features should be enabled as best practices for MAB? (Choose three.)',
        ['MD5', 'storm control', 'URPF'],
        'IP source guard', 'DHCP snooping', 'DAI'),
    QA('When MAB is configured, how often are ports reauthenticated by default?',
        ['every 60 seconds', 'every 90 seconds', 'every 120 seconds'],
        'Never'),
    QA('What is a required step when you deploy dynamic VLAN and ACL assignments?',
        ['Configure the VLAN assignment.', 'Configure the ACL assignment.',
         'Configure the Cisco IOS Software switch for ACL assignment.'],
        'Configure Cisco IOS Software 802.1X authenticator authorization.'),
    QA('Which model does Cisco support in a RADIUS change of authorization implementation?',
        ['pull', 'policy', 'security'], 'push'),
    QA('An organization has recently deployed ISE with the latest models of Cisco switches, and it plans to deploy Trustsec to secure its infrastructure. '
        'The company also wants to allow different network access policies for different user groups (e.g., administrators). '
        'Which solution is needed to achieve these goals?',
        ['MACsec in Multiple-Host Mode in order to open or close a port based on a single authentication',
         'Identity-based ACLs on the switches with user identities provided by ISE',
         'Cisco Threat Defense for user group control by leveraging Netflow exported from the switches and login information from ISE'],
        'Cisco Security Group Access Policies in order to use SGACLs to control access based on SGTs assigned to different users'),
    QA('Security Group Access requires which three syslog messages to be sent to Cisco ISE? (Choose three.)',
        ['IOS-7-PROXY_DROP', 'MKA-2-MACDROP', 'ASA-6-CONNECT_BUILT'],
        'AP-1-AUTH_PROXY_DOS_ATTACK', 'AUTHMGR-5-MACMOVE',
        'AP-1-AUTH_PROXY_FALLBACK_REQ'),
    QA('Which administrative role has permission to assign Security Group Access Control Lists?',
        ['System Admin', 'Network Device Admin', 'Identity Admin'],
        'Policy Admin'),
    QA('If the given configuration is applied to the object-group vpnservers, during which time period are external users able to connect?',
        ['From Friday at 6:01 p.m. until Monday at 8:01 a.m.',
         'From Monday at 8:00 a.m. until Friday at 6:00 p.m.',
         'From Friday at 6:00 p.m. until Monday at 8:00 a.m.'],
        'From Monday at 8:01 a.m. until Friday at 5:59 p.m.'),
    QA('Which set of commands allows IPX inbound on all interfaces?',
        ['ASA1(config)# access-list IPX-Allow ethertype permit ipx'
         'ASA1(config)# access-group IPX-Allow in interface inside',
         'ASA1(config)# access-list IPX-Allow ethertype permit ipx'
         'ASA1(config)# access-group IPX-Allow in interface outside',
         'ASA1(config)# access-list IPX-Allow ethertype permit ipx'
         'ASA1(config)# access-group IPX-Allow out interface global'],
        'ASA1(config)# access-list IPX-Allow ethertype permit ipx'
        'ASA1(config)# access-group IPX-Allow in interface global'),
    QA('Which command enables static PAT for TCP port 25?',
        ['static (inside,outside) 209.165.201.3 209.165.201.226 netmask 255.255.255.255',
         'nat static 209.165.201.3 eq smtp',
         'nat (outside,inside) static 209.165.201.3 209.165.201.226 eq smtp'],
        'nat (inside,outside) static 209.165.201.3 service tcp smtp smtp'),
    QA('Which command is useful when troubleshooting AAA Authentication between a Cisco router and the AAA server?',
        ['test aaa-server tacacs+ group7 cisco cisco123 new-code',
         'test aaa group7 tacacs+ auth cisco123 new-code',
         'test aaa-server test cisco cisco123 all new-code'],
        'test aaa group tacacs+ cisco cisco123 new-code'),
    QA('In a multi-node ISE deployment, backups are not working on the MnT node. Which ISE CLI option would help mitigate this issue?',
        ['collector',
         'application-bundle',
         'ftp-url'],
        'repository'),
    QA('Which command can check a AAA server authentication for server group Group1, user cisco, and password cisco555 on a Cisco ASA device?',
        ['ASA# aaa-server authentication Group1 roger cisco555',
         'ASA# aaa-server authorization Group1 username cisco password cisco555',
         'ASA# test aaa-server authentication group Group1 username cisco password cisco555'],
        'ASA# test aaa-server authentication Group1 username cisco password cisco555'),
    QA('Which statement about system time and NTP server configuration with Cisco ISE is true?',
        ['The system time and NTP server settings can be configured centrally on the Cisco ISE.',
         'The system time can be configured centrally on the Cisco ISE, but NTP server settings must be configured individually on each ISE node.',
         'NTP server settings can be configured centrally on the Cisco ISE, but the system time must be configured individually on each ISE node.'],
        'The system time and NTP server settings must be configured individually on each ISE node.'),
    QA('Wireless client supplicants attempting to authenticate to a wireless network are generating excessive log messages. Which three WLC authentication settings should be disabled? (Choose three.)',
        ['Roaming', 'Client Exclusion', 'RADIUS Server Timeout'],
        'Session Timeout', 'Idle Timer', 'RADIUS Aggressive-Failover'),
    QA('Which two authentication stores are supported to design a wireless network using PEAP EAP-MSCHAPv2 as the authentication method? (Choose two.)',
        ['Certificate Server', 'RSA Secure-ID', 'LDAP'],
        'ACS', 'Microsoft Active Directory'),
    QA('What is another term for 802.11i wireless network security?',
        ['802.1x', 'WEP', 'TKIP', 'WPA'], 'WPA2'),
    QA('Which two EAP types require server side certificates? (Choose two.)',
        ['EAP-MD5', 'LEAP', 'MSCHAPv2', 'EAP-FAST'], 'PEAP', 'EAP-TLS'),
    QA('Where is client traffic decrypted in a controller-based wireless network protected with WPA2 Security?',
        ['Authentication Server', 'Wireless LAN Controller', 'Switch'],
        'Access Point'),
    QA('Which setting provides the best security for a WLAN and authenticates users against a centralized directory store?',
        ['WPA2 TKIP and 802.1X authentication',
         'WPA2 TKIP and PSK authentication',
         'WPA2 AES-CCMP and PSK authentication'],
        'WPA2 AES-CCMP and 801.X authentication'),
    QA('What is a feature of Cisco WLC and IPS synchronization?',
        ['Cisco WLC populates the ACLs to prevent repeat intruder attacks.',
         'Cisco WLC and IPS synchronization enables faster wireless access.',
         'IPS synchronization uses network access points to provide reliable monitoring.'],
        'The IPS automatically send shuns to Cisco WLC for an active host block.'),
    QA('Which two components are required to connect to a WLAN network that is secured by EAP-TLS authentication? (Choose two.)',
        ['Kerberos authentication server', 'PSKs'],
        'AAA/RADIUS server', 'CA server'),
    QA('Which statement about Cisco Management Frame Protection is true?',
        ['It identifies potential RF jamming attacks.',
         'It detects spoofed MAC addresses.',
         'It enables stations to remain in power-save mode, except at specified intervals to receive data from the access point.'],
        'It protects against frame and device spoofing.'),
    QA('Which three statements about the Cisco wireless IPS solution are true? (Choose three.)',
        ['It allows the WLC to failover because of congestion.',
         'It enables stations to remain in power-save mode, except at specified intervals to receive data from the access point.'],
        'It detects spoofed MAC addresses.',
        'It identifies potential RF jamming attacks.',
        'It protects against frame and device spoofing.'),
    QA('In a basic ACS deployment consisting of two servers, for which three tasks is the primary server responsible? (Choose three.)',
        ['sensing', 'monitoring', 'repudiation'],
        'configuration', 'authentication', 'policy requirements'),
    QA('In a split ACS deployment with primary and secondary servers, which three statements about AAA load handling are true? (Choose three.)',
        ['The primary servers are used to distribute policy information to other servers in the enterprise.',
         'During normal operations, each server processes the full workload of both servers.',
         'If a AAA connectivity problem occurs, the servers split the full load of authentication requests.'],
        'If a AAA connectivity problem occurs, each server processes the full workload of both servers.',
        'During normal operations, the servers split the full load of authentication requests.',
        'During normal operations, each server is used for specific operations, such as device administration and network admission.'),
    QA('Which three personas can a Cisco ISE assume in a deployment? (Choose three.)',
        ['testing', 'authentication', 'connection'],
        'monitoring', 'policy service', 'administration'),
    QA('Which three components comprise the Cisco ISE profiler? (Choose three.)',
        ['a remitter tool, which fails over to redundant profilers',
         'the trigger, which activates ACLs',
         'a monitoring tool that connects to the Cisco ISE'],
        'an analyzer, which uses configured policies to evaluate endpoints',
        'the probe manager',
        'the sensor, which contains one or more probes'),
    QA('Which three statements about the Cisco ISE profiler are true? (Choose three.)',
        ['It monitors and polices router and firewall traffic.',
         'It stores MAC addresses for endpoint systems.',
         'It sends endpoint data to AAA servers.'],
        'It stores endpoints in the Cisco ISE database with their profiles.',
        'It matches endpoints to their profiles.',
        'It collects endpoint attributes.'),
    QA('From which location can you run reports on endpoint profiling?',
        ['Operations > Catalog > Endpoint',
         'Operations > Catalog > Reports > Endpoint',
         'Reports > Operations > Catalog > Endpoint'],
        'Operations > Reports > Catalog > Endpoint'),
    QA('Which two services are included in the Cisco ISE posture service? (Choose two.)',
        ['posture catalog', 'posture policing', 'posture monitoring'],
        'posture run-time', 'posture administration'),
    QA('What is a requirement for posture administration services in Cisco ISE?',
        ['an ACL that points traffic to the Cisco ISE deployment',
         'Cisco NAC Agents that communicate with the Cisco ISE server',
         'at least one Cisco router to store Cisco ISE profiling policies'],
        'the advanced license package must be installed'),
    QA('Which two statements about Cisco NAC Agents that are installed on clients that interact with the Cisco ISE profiler are true? (Choose two.)',
        ['They store endpoints in the Cisco ISE with their profiles.',
         'They block access from the network through noncompliant endpoints.',
         'They collect endpoint attributes.',
         'They send endpoint data to AAA servers.'],
        'They interact with the posture service to enforce endpoint security policies.',
        'They evaluate clients against posture policies, to enforce requirements.'),
    QA('What steps must you perform to deploy a CA-signed identify certificate on an ISE device?',
        ['1. Download the CA server certificate.\n'
         '2. Generate a signing request and save it as a file.\n'
         '3. Access the CA server and submit the ISE request.\n'
         '4. Install the issued certificate on the ISE.',
         '1. Download the CA server certificate.\n'
         '2. Generate a signing request and save it as a file.\n'
         '3. Access the CA server and submit the ISE request.\n'
         '4. Install the issued certificate on the CA server.',
         '1. Generate a signing request and save it as a file.\n'
         '2. Download the CA server certificate.\n'
         '3. Access the ISE server and submit the CA request.\n'
         '4. Install the issued certificate on the CA server.'],
        '1. Generate a signing request and save it as a file.\n'
        '2. Download the CA server certificate.\n'
        '3. Access the CA server and submit the ISE request.\n'
        '4. Install the issued certificate on the ISE.'),
    QA('What implementation must be added to the WLC to enable 802.1X and CoA for wireless endpoints?',
        ['a policy server', 'a router', 'an ACL'], 'the ISE'),
    QA('What are the initial steps must you perform to add the ISE to the WLC?',
        ['1. With a Web browser, establish an HTTP connection to the WLC pod.\n'
         '2. Navigate to Administration > Authentication > New.\n'
         '3. Enter server values to begin the configuration.',
         '1. With a Web browser, establish an FTP connection to the WLC pod.\n'
         '2. Navigate to Security > Administration > New.\n'
         '3. Add additional security features for FTP authentication.',
         '1. With a Web browser, establish an HTTP connection to the WLC pod.\n'
         '2. Navigate to Authentication > New.\n'
         '3. Enter ACLs and Authentication methods to begin the configuration.'],
        '1. With a Web browser connect, establish an HTTPS connection to the WLC pod.\n'
        '2. Navigate to Security > Authentication > New.\n'
        '3. Enter server values to begin the configuration'),
    QA('Which command configures console port authorization under line con 0?',
        ['authorization default|WORD', 'authorization exec line con 0|WORD',
         'authorization line con 0|WORD'],
        'authorization exec default|WORD'),
    QA('Which two statements about administrative access to the ACS Solution Engine are true? (Choose two.)',
        ['The ACS Solution Engine supports command-line connections through a serial-port connection.',
         'The ACS Solution Engine supports command-line connections through an Ethernet interface.',
         'GUI access to the ACS Solution Engine is not supported.'],
        'For GUI access, an administrative GUI user must be created with the add-guiadmin command.',
        'An ACL-based policy must be configured to allow administrative-user access.'),
    QA('What is the purpose of the Cisco ISE Guest Service Sponsor Portal?',
        ['It tracks and stores user activity while connected to the Cisco ISE.',
         'It securely authenticates guest users for the Cisco ISE Guest Service.',
         'It filters guest users from account holders to the Cisco ISE.'],
        'It creates and manages Guest User accounts.'),
    QA('What is the effect of the ip http secure-server command on a Cisco ISE?',
        ['It enables the HTTP server for users to connect on the command line.',
         'It enables the HTTP server for users to connect using Web-based authentication.',
         'It enables the HTTPS server for users to connect on the command line.'],
        'It enables the HTTPS server for users to connect using Web-based authentication.'),
    QA('When RADIUS NAC and AAA Override are enabled for WLC on a Cisco ISE, which two statements about RADIUS NAC are true? (Choose two.)',
        ['It will return an access-accept and send the redirection URL for all users.',
         'It establishes secure connectivity between the RADIUS server and the ISE.',
         'It allows multiple users to authenticate at the same time.'],
        'It allows the ISE to send a CoA request that indicates when the user is authenticated.',
        'It is used for posture assessment, so the ISE changes the user profile based on posture result.'),
    QA('What are the initial steps to configure an ACS as a TACACS server?',
        ['1. Choose Network Devices and AAA Clients > Network Resources.\n'
         '2. Click Create.',
         '1. Choose Network Resources > Network Devices and AAA Clients.\n'
         '2. Click Manage.',
         '1. Choose Network Devices and AAA Clients > Network Resources.\n'
         '2. Click Install'],
        '1. Choose Network Resources > Network Devices and AAA Clients.\n'
        '2. Click Create.'),
    QA('Which two statements about administrative access to the Cisco Secure ACS SE are true? (Choose two.)',
        ['The Cisco Secure ACS SE supports command-line connections through a serial-port connection.',
         'The Cisco Secure ACS SE supports command-line connections through an Ethernet interface.',
         'GUI access to the Cisco Secure ASC SE is not supported.'],
        'For GUI access, an administrative GUI user must be created by using the add-guiadmin command.',
        'An ACL-based policy must be configured to allow administrative-user access.'),
    QA('When RADIUS NAC and AAA Override are enabled for a WLC on a Cisco ISE, which two statements about RADIUS NAC are true? (Choose two.)',
        ['It returns an access-accept and sends the redirection URL for all users.',
         'It establishes secure connectivity between the RADIUS server and the Cisco ISE.',
         'It allows multiple users to authenticate at the same time.'],
        'It allows the Cisco ISE to send a CoA request that indicates when the user is authenticated.',
        'It is used for posture assessment, so the Cisco ISE changes the user profile based on posture result.'),
    QA('In an 802.1X authorization process, a network access device provides which three functions? (Choose three.)',
        ['Hosts a central web authentication page',
         'Confirms supplicant protocol compliance',
         'Validates authentication credentials'],
        'Filters traffic prior to authentication',
        'Passes credentials to authentication server',
        'Enforces policy provided by authentication server'),
    QA('Which two switchport commands enable MAB and allow non-802.1X capable devices to immediately run through the MAB process? (Choose two.)',
        ['authentication order dot1x mab',
         'no authentication timer',
         'dot1x timeout tx-period',
         'authentication open'],
        'authentication order mab dot1x',
        'mab'),
    QA('Which two attributes must match between two Cisco ASA devices to properly enable high availability? (Choose two.)',
        ['tcp dead-peer detection protocol', '802.1x authentication identity'],
        'model, interface configuration, and RAM',
        'major and minor software release'),
    QA('What are two client-side requirements of the NAC Agent and NAC Web Agent installation? (Choose two.)',
        ['Active Directory Domain membership',
         'WSUS service running'],
        'Administrator workstation rights',
        'Allowing of web browser activex installation'),
    QA('Which three algorithms should be avoided due to security concerns? (Choose three.)',
        ['AES GCM mode for encryption',
         'HMAC-SHA-1',
         '256-bit Elliptic Curve Diffie-Hellman',
         '2048-bit Diffie-Hellman'],
        'DES for encryption',
        'SHA-1 for hashing',
        '1024-bit RSA'),
    QA('Which statement about IOS accounting is true?',
        ['A named list of AAA methods must be defined.',
         'A named list of accounting methods must be defined.',
         'A named list of tracking methods must be defined.'],
        'Authorization must be configured before accounting.'),
    QA('Which effect does the ip http secure-server command have on a Cisco ISE?',
        ['It enables the HTTP server for users to connect on the command line.',
         'It enables the HTTP server for users to connect by using web-based authentication.',
         'It enables the HTTPS server for users to connect on the command line.'],
        'It enables the HTTPS server for users to connect by using web-based authentication.'),
    QA('The NAC Agent v4.9.x uses which ports and protocols to communicate with an ISE Policy Service Node?',
        ['tcp/8905, http/80, ftp/21',
         'udp/8905, telnet/23, https/443',
         'udp/8906, http/80, https/443'],
        'tcp/8905, http/80, https/443'),
    QA('Which two are valid ISE posture conditions? (Choose two.)',
        ['Dictionary',
         'memberOf',
         'Profile status'],
        'File',
        'Service'),
    QA('A network engineer is configuring HTTP based CWA on a switch. Which three configuration elements are required? (Choose three.)',
        ['Redirect-URL',
         'HTTP secure server enabled',
         'Radius authentication on the port with 802.1x',
         'Pre-auth port based access-list'],
        'HTTP server enabled',
        'Radius authentication on the port with MAB',
        'Redirect access-list'),
    QA('Which three statements describe differences between TACACS+ and RADIUS? (Choose three.)',
        ['RADIUS encrypts the entire packet, while TACACS+ encrypts only the password.',
         'RADIUS uses TCP, while TACACS+ uses UDP.',
         'TACACS+ uses ports 1812 and 1813, while RADIUS uses port 49.'],
        'TACACS+ encrypts the entire packet, while RADIUS encrypts only the password.',
        'TACACS+ uses TCP, while RADIUS uses UDP.',
        'RADIUS uses ports 1812 and 1813, while TACACS+ uses port 49.'),
    QA('Which two identity store options allow you to authorize based on group membership? (Choose two).',
        ['RSA SecurID server', 'RADIUS'],
        'Lightweight Directory Access Protocol', 'Active Directory'),
    QA('What attribute could be obtained from the SNMP query probe?',
        ['FQDN', 'DHCP class identifier', 'User agent'], 'CDP'),
    QA('What is a required configuration step for an 802.1X capable switch to support dynamic VLAN and ACL assignments?',
        ['Configure the VLAN assignment.',
         'Configure the ACL assignment.',
         'Configure port security on the switch port.'],
        'Configure 802.1X authenticator authorization.'),
    QA('Which network component would issue the CoA?',
        ['switch', 'endpoint', 'Admin Node'], 'Policy Service Node'),
    QA('What steps must you perform to deploy a CA-signed identity certificate on an ISE device?',
        ['1. Download the CA server certificate and install it on ISE.\n'
         '2. Generate a signing request and save it as a file.\n'
         '3. Access the CA server and submit the CA request.\n'
         '4. Install the issued certificate on the ISE.',
         '1. Download the CA server certificate and install it on ISE.\n'
         '2. Generate a signing request and save it as a file.\n'
         '3. Access the CA server and submit the CSR.\n'
         '4. Install the issued certificate on the CA server.',
         '1. Generate a signing request and save it as a file.\n'
         '2. Download the CA server certificate and install it on ISE.\n'
         '3. Access the ISE server and submit the CA request.\n'
         '4. Install the issued certificate on the CA server.'],
        '1. Generate a signing request and save it as a file.\n'
        '2. Download the CA server certificate and install it on ISE.\n'
        '3. Access the CA server and submit the CSR.\n'
        '4. Install the issued certificate on the ISE.'),
    QA('An organization has recently deployed ISE with Trustsec capable Cisco switches and would like to allow differentiated network access based on user groups.\n'
        'Which solution is most suitable for achieving these goals?',
        ['Cyber Threat Defense for user group control by leveraging Netflow exported from the Cisco switches and identity information from ISE',
         'MACsec in Multiple-Host Mode in order to encrypt traffic at each hop of the network infrastructure',
         'Identity-based ACLs preconfigured on the Cisco switches with user identities provided by ISE'],
        'Cisco Security Group Access Policies to control access based on SGTs assigned to different user groups'),
    QA('Which three are required steps to enable SXP on a Cisco ASA? (Choose three).',
        ['configure AAA authentication',
         'issue the aaa authorization command aaa-server group command',
         'configure TACACS'],
        'configure password',
        'configure a peer',
        'issue the cts sxp enable command'),
    QA('Which three network access devices allow for static security group tag assignment? (Choose three.)',
        ['intrusion prevention system',
         'load balancer',
         'wireless LAN controller'],
        'access layer switch',
        'data center access switch',
        'VPN concentrator'),
    QA('Which option is required for inline security group tag propagation?',
        ['Cisco Secure Access Control System',
         'Security Group Tag Exchange Protocol (SXP) v4',
         'Cisco Identity Services Engine'],
        'hardware support'),
    QA('Which two fields are characteristics of IEEE 802.1AE frame? (Choose two.)',
        ['destination MAC address',
         'source MAC address',
         'security group tag in EtherType',
         'CRC/FCS'],
        '802.1AE header in EtherType',
        'integrity check value'),
    QA('Which two options are valid for configuring IEEE 802.1AE MACSec between switches in a TrustSec network? (Choose two.)',
        ['in the Cisco Identity Services Engine',
         'in the global configuration of a TrustSec non-seed switch',
         'in the Cisco Secure Access Control System',
         'in the global configuration of a TrustSec seed switch'],
        'manually on links between supported switches',
        'dynamically on links between supported switches'),
    QA('Which three pieces of information can be found in an authentication detail report? (Choose three.)',
        ['DHCP vendor ID',
         'user agent string',
         'failed posture requirement'],
        'the authorization rule matched by the endpoint',
        'the EAP method the endpoint is using',
        'the RADIUS username being used'),
    QA('Certain endpoints are missing DHCP profiling data.\n'
        'Which option describes what can be used to determine if DHCP requests from clients are reaching Cisco ISE?',
        ['output of show interface gigabitEthernet 0 from the CLI',
         'output of debug logging all 7 from the CLI',
         'output of show logging application profiler.log from the CLI',
         'the posture troubleshooting diagnostic tool through the GUI'],
        'the TCP dump diagnostic tool through the GUI'),
    QA('Which debug command on a Cisco WLC shows the reason that a client session was terminated?',
        ['debug dot11 state enable',
         'debug dot1x packet enable',
         'debug dtls event enable',
         'debug ap enable cisco ap'],
        'debug client mac addr'),
    QA('Which two identity databases are supported when PEAP-MSCHAPv2 is used as EAP type? (Choose two.)',
        ['LDAP',
         'RADIUS token server',
         'internal endpoint store',
         'certificate authentication profile',
         'RSA SecurID'],
        'Windows Active Directory',
        'internal user store'),
    QA('Which two Cisco Catalyst switch interface commands allow only a single voice device and a single data device to be connected to the IEEE 802.1X-enabled interface? (Choose two.)',
        ['authentication host-mode multi-host',
         'authentication host-mode multi-auth'],
        'authentication host-mode single-host',
        'authentication host-mode multi-domain'),
    QA('Which RADIUS attribute is used primarily to differentiate an IEEE 802.1x request from a Cisco MAB request?',
        ['RADIUS Attribute (5) NAS-Port',
         'RADIUS Attribute (7) Framed-Protocol',
         'RADIUS Attribute (61) NAS-Port-Type'],
        'RADIUS Attribute (6) Service-Type'),
    QA('Which authorization method is the Cisco best practice to allow endpoints access to the Apple App store or Google Play store with Cisco WLC software version 7.6 or newer?',
        ['dACL', 'DNS ACL defined in Cisco ISE', 'redirect ACL'], 'DNS ACL'),
    QA('Which time allowance is the minimum that can be configured for posture reassessment interval?',
        ['5 minutes', '20 minutes', '90 minutes'], '60 minutes'),
    QA('Which advanced authentication setting is needed to allow an unknown device to utilize Central WebAuth?',
        ['If Authentication failed > Continue',
         'If Authentication failed > Drop',
         'If user not found > Reject'],
        'If user not found > Continue'),
    QA('Which option restricts guests from connecting more than one device at a time?',
        ['Guest Portal policy > Set Device registration portal limit',
         'My Devices Portal > Set Maximum number of devices to register',
         'Multi-Portal Policy > Guest users should be able to do device registration'],
        'Guest Portal Policy > Set Allow only one guest session per user'),
    QA('In Cisco ISE, which two actions can be taken based on matching a profiler policy? (Choose two).',
        ['delete endpoint',
         'automatically remediate',
         'create matching identity group'],
        'exception',
        'network scan (NMAP)'),
    QA('Which statement about the Cisco ISE BYOD feature is true?',
        ['BYOD works only on wireless access.',
         'Cisco ISE needs to integrate with MDM to support BYOD.',
         'Only mobile endpoints are supported.'],
        'Use of SCEP/CA is optional.'),
    QA('What user rights does an account need to join ISE to a Microsoft Active Directory domain?',
        ['Domain Admin',
         'Join and Leave Domain',
         'Create and Delete User Objects'],
        'Create and Delete Computer Objects'),
    QA('A network administrator must enable which protocol to utilize EAP-Chaining?',
        ['EAP-TLS',
         'MSCHAPv2',
         'PEAP'],
        'EAP-FAST'),
    QA('The corporate security policy requires multiple elements to be matched in an authorization policy.\n'
        'Which elements can be combined to meet the requirement?',
        ['Device registration status and device activation status',
         'User credentials and server certificate',
         'Built-in profile and custom profile'],
        'Network access device and time condition'),
    QA('A network administrator needs to determine the ability of existing network devices to deliver key BYOD services. Which tool will complete a readiness assessment and outline hardware and software capable and incapable devices?',
        ['Network Control System',
         'Cisco Security Manager',
         'Identity Services Engine'],
        'Prime Infrastructure'),
    QA('Which EAP method uses a modified version of the MS-CHAP authentication protocol?',
        ['EAP-POTP', 'EAP-TLS', 'EAP-MD5'], 'LEAP'),
    QA('Under which circumstance would an inline posture node be deployed?',
        ['When the NAD cannot support the number of connected endpoints',
         'When a PSN is overloaded',
         'To provide redundancy for a PSN'],
        'When the NAD does not support CoA'),
    QA('Which Cisco ISE 1.x protocol can be used to control admin access to network access devices?',
        ['TACACS+',
         'EAP',
         'Kerberos'],
        'RADIUS'),
    QA('A user is on a wired connection and the posture status is noncompliant.\n'
        'Which state will their EPS session be placed in?',
        ['disconnected', 'limited', 'no access'], 'quarantined'),
    QA('Which three posture states can be used for authorization rules? (Choose three.)',
        ['known',
         'quarantined',
         'no access',
         'limited'],
        'unknown',
        'noncompliant',
        'compliant'),
    QA('Which two Cisco ISE administration options are available in the Default Posture Status setting? (Choose two.)',
        ['Unknown',
         'FailOpen',
         'FailClose'],
        'Compliant',
        'Noncompliant'),
    QA('Which two portals can be configured to use portal FQDN? (Choose two.)',
        ['admin',
         'guest',
         'monitoring and troubleshooting'],
        'sponsor',
        'my devices'),
    QA('Which five portals are provided by PSN? (Choose five.)',
        ['admin',
         'monitoring and troubleshooting'],
        'guest',
        'sponsor',
        'my devices',
        'blacklist',
        'client provisioning'),
    QA('When you add a new PSN for guest access services, which two options must be enabled under deployment settings? (Choose two.)',
        ['Admin', 'Monitoring', 'Profiling'], 'Policy Service',
        'Session Services'),
    QA('In Cisco ISE, which probe must be enabled to collect profiling data using Device Sensor?',
        ['SNMPQuery', 'SNMPTrap', 'Network Scan', 'Syslog'], 'RADIUS'),
    QA('Which two profile attributes can be collected by a Cisco Catalyst Switch that supports Device Sensor? (Choose two.)',
        ['user agent', 'open ports', 'operating system', 'trunk ports'],
        'LLDP agent information', 'DHCP options'),
    QA('Which two profile attributes can be collected by a Cisco Wireless LAN Controller that supports Device Sensor? (Choose two.)',
        ['LLDP agent information', 'open ports',
         'CDP agent information', 'FQDN'],
        'user agent', 'DHCP options'),
    QA('Which statement about Cisco ISE BYOD is true?',
        ['Dual SSID allows EAP-TLS only when connecting to the secured SSID.',
         'Single SSID does not require endpoints to be registered.',
         'Dual SSID allows BYOD for guest users.',
         'Single SSID utilizes open SSID to accommodate different types of users.'],
        'Single SSID allows PEAP-MSCHAPv2 for native supplicant provisioning.'),
    QA('Which two types of client provisioning resources are used for BYOD implementations? (Choose two.)',
        ['user agent',
         'Cisco NAC agent',
         'device sensor'],
        'native supplicant profiles',
        'software provisioning wizards'),
    QA('Which protocol sends authentication and accounting in different requests?',
        ['RADIUS',
         'EAP-Chaining',
         'PEAP',
         'EAP-TLS'],
        'TACACS+'),
    QA('You enabled the guest session limit feature on the Cisco ISE. However, end users report that the same guest can log in from multiple devices simultaneously.\n'
        'Which configuration is missing on the network access device?',
        ['RADIUS authentication',
         'DHCP required',
         'AAA override'],
        'RADIUS accounting'),
    QA('A properly configured Cisco ISE Policy Service node is not receiving any profile data from a Cisco switch that runs Device Sensor.\n'
        'Which option is the most likely reason for the failure?',
        ['Syslog is configured for the Policy Administration Node.',
         'The SNMP community strings are mismatched.',
         'RADIUS Authentication is misconfigured.',
         'The connected endpoints support CDP but not DHCP.'],
        'RADIUS Accounting is disabled.'),
    QA('Changes were made to the ISE server while troubleshooting, and now all wireless certificate authentications are failing. Logs indicate an EAP failure.\n'
        'What are the two possible causes of the problem? (Choose two.)',
        ['Client certificate is not included in the Trusted Certificate Store',
         'MS-CHAPv2-is not checked in the Allowed Protocols list',
         'Default rule denies all traffic'],
        'EAP-TLS is not checked in the Allowed Protocols list',
        'Certificate authentication profile is not configured in the Identity Store'),
    QA('Which action must an administrator take after joining a Cisco ISE deployment to an Active Directory domain?',
        ['Choose an Active Directory user.',
         'Configure the management IP address.',
         'Configure replication.'],
        'Choose an Active Directory group.'),
    QA('Which feature of Cisco ASA allows VPN users to be postured against Cisco ISE without requiring an inline posture node?',
        ['device tracking',
         'DHCP snooping',
         'VLAN hopping'],
        'RADIUS Change of Authorization'),
    QA('After an endpoint has completed authentication with MAB, a security violation is triggered because a different MAC address was detected.\n'
        'Which host mode must be active on the port?',
        ['multidomain authentication host mode',
         'multiauthentication host mode',
         'multihost mode'],
        'single-host mode'),
    QA('You are configuring permissions for a new Cisco ISE standard authorization profile. If you configure the Tunnel-Private-Group-ID attribute as shown, what does the value 123 represent?',
        ['the VRF ID', 'the tunnel ID', 'the group ID'], 'the VLAN ID'),
    QA('Where would a Cisco ISE administrator define a named ACL to use in an authorization policy?',
        ['In the conditions of an authorization rule.',
         'In the attributes of an authorization rule.',
         'In the permissions of an authorization rule.'],
        'In an authorization profile associated with an authorization rule.'),
    QA('Which URL must you enter in the External Webauth URL field to configure Cisco ISE CWA correctly?',
        ['https://ip_address:443/guestportal/Welcome.html',
         'https://ip_address:443/guestportal/action=cpp',
         'https://ip_address:8905/guestportal/Sponsor.action'],
        'https://ip_address:8443/guestportal/Login.action'),
    QA('When you configure an endpoint profiling policy rule, which option describes the purpose of the minimum certainty factor?',
        ['It is compared to the assigned certainty value of an individual endpoint in a device database to determine whether the endpoint can be trusted.',
         'It is used to compare the policy condition to other active policies.',
         'It is used to determine the likelihood that an endpoint is an active, trusted device on the network.'],
        'It is compared to the total certainty metric of an individual endpoint to determine whether the endpoint can be trusted.'),
    QA('You have configured a Cisco ISE 1.2 deployment for self-registration of guest users.\n'
        'What two options can you select from to determine when the account duration timer begins? (Choose two.)',
        ['BeginLogin', 'StartTime'], 'CreateTime', 'FirstLogin'),
    QA('Which error in a redirect ACL can cause the redirection of an endpoint to the provisioning portal to fail?',
        ['The redirect ACL is applied to an incorrect SVI.',
         'The redirect ACL is blocking access to the client provisioning portal.',
         'The redirect ACL is blocking access to Cisco ISE port 8905.'],
        'The redirect ACL is blocking access to ports 80 and 443.'),
    QA('Where must periodic re-authentication be configured to allow a client to come out of the quarantine state and become compliant?',
        ['on the router port',
         'on the supplicant',
         'on the controller'],
        'on the switch port'),
    QA('Which functionality does the Cisco ISE self-provisioning flow provide?',
        ['It provides the My Devices portal, allowing users to add devices to the network.',
         'It provides support for users to install the Cisco NAC agent on enterprise devices.',
         'It provides self-registration functionality to allow guest users to access the network.'],
        'It provides support for native supplicants, allowing users to connect devices directly to the network.'),
    QA('During client provisioning on a Mac OS X system, the client system fails to renew its IP address.\n'
        'Which change can you make to the agent profile to correct the problem?',
        ['Enable the Enable VLAN Detect Without UI feature.',
         'Enable CRL checking.',
         'Edit the Discovery Host parameter to use an IP address instead of an FQDN.'],
        'Enable the Agent IP Refresh feature.'),
    QA('Where is dynamic SGT classification configured?',
        ['NAD', 'supplicant', 'RADIUS proxy'], 'Cisco ISE'),
    QA('What is the function of the SGACL policy matrix on a Cisco TrustSec domain with SGT Assignment?',
        ['It determines which switches are trusted within the TrustSec domain.',
         'It determines the path the SGT of the packet takes when entering the Cisco TrustSec domain.',
         'It lists all servers that are permitted to participate in the TrustSec domain.',
         'It lists all hosts that are permitted to participate in the TrustSec domain.'],
        'It determines which access policy to apply to the endpoint.'),
    QA('You are configuring SGA on a network device that is unable to perform SGT tagging. How can the device propagate SGT information?',
        ['The device can use SXP to pass MAC-address-to-STG mappings to a TrustSec-capable hardware peer.',
         'The device can use SXP to pass MAC-address-to-IP mappings to a TrustSec-capable hardware peer.',
         'The device can propagate SGT information in an encapsulated security payload.',
         'The device can use a GRE tunnel to pass the SGT information to a TrustSec-capable hardware peer.'],
        'The device can use SXP to pass IP-address-to-SGT mappings to a TrustSec-capable hardware peer.'),
    QA('The links outside the TrustSec area in the given SGA architecture are unprotected. On which two links does EAC take place? (Choose two.)',
        ['between host 1 and switch 1',
         'between the authentication server and switch 4',
         'between switch 1 and switch 2',
         'between switch 1 and switch 5'],
        'between switch 2 and switch 3',
        'between switch 5 and host 2'),
    QA('Which three host modes support MACsec? (Choose three.)',
        ['multi-MAC host mode',
         'dual-host mode',
         'multi-auth host mode'],
        'multidomain authentication host mode',
        'multihost mode',
        'single-host mode'),
    QA('You are troubleshooting wired 802.1X authentications and see the following error: "Authentication failed: 22040 Wrong password or invalid shared secret." What should you inspect to determine the problem?',
        ['Active Directory shared secret',
         'Identity source sequence',
         'TACACS+ shared secret',
         'Certificate authentication profile'],
        'RADIUS shared secret'),
    QA('You are troubleshooting RADIUS issues on the network and the debug radius command returns the given output. What is the most likely reason for the failure?',
        ['The RADIUS port is incorrect.',
         'The NAD is untrusted by the RADIUS server.',
         'The RADIUS server is unreachable.',
         'RADIUS shared secret does not match'],
        'An invalid username or password was entered.'),
    QA('What are two possible reasons why a scheduled nightly backup of ISE to a FTP repository would fail? (Choose two.)',
        ['The ISE and FTP server clocks are out of sync.',
         'The server key is invalid or misconfigured.',
         'TCP port 69 is disabled on the FTP server.'],
        'ISE attempted to write the backup to an invalid path on the FTP server.',
        'The username and password for the FTP server are invalid.'),
    QA('Which two statements about MAB are true? (Choose two.)',
        ['It is unable to control network access at the edge.',
         'If MAB fails, the device is unable to fall back to another authentication method.',
         'It is unable to link the IP and MAC addresses of a device.'],
        'It requires a preexisting database of the MAC addresses of permitted devices.',
        'It is unable to authenticate individual users.'),
    QA('Which type of access list is the most scalable that Cisco ISE can use to implement network authorization enforcement for a large number of users?',
        ['named access lists',
         'VLAN access lists',
         'MAC address access lists'],
        'downloadable access lists'),
    QA('When you select Centralized Web Auth in the ISE Authorization Profile, which two components host the web authentication portal? (Choose two.)',
        ['ISE',
         'the access point',
         'the endpoints'],
        'the WLC',
        'the switch'),
    QA('What is the default posture status for non-agent capable devices, such as Linux and iDevices?',
        ['Unknown',
         'Validated',
         'Default'],
        'Compliant'),
    QA('Your guest-access wireless network is experiencing degraded performance and excessive latency due to user saturation.\n'
        'Which type of rate limiting can you implement on your network to correct the problem?',
        ['per-policy',
         'per-access point',
         'per-controller',
         'per-application'],
        'per-device'),
    QA('You are installing Cisco ISE on nodes that will be used in a distributed deployment. After the initial bootstrap process, what state will the Cisco ISE nodes be in?',
        ['Remote',
         'Policy service',
         'Administration'],
        'Standalone'),
    QA('What three changes require restarting the application service on an ISE node? (Choose three.)',
        ['Installing the root CA certificate.',
         'Changing the guest portal default port settings.',
         'Adding a network access device.'],
        'Registering a node.',
        'Changing the primary node to standalone.',
        'Promoting the administration node.'),
    QA('Which default identity source is used by the MyDevices_Portal_Sequence identity source sequence?',
        ['guest users',
         'Active Directory',
         'internal endpoints',
         'RADIUS servers'],
        'internal users'),
    QA('What EAP method supports mutual certificate-based authentication?',
        ['EAP-TTLS',
         'EAP-MSCHAP',
         'EAP-MD5'],
        'EAP-TLS'),
    QA('Which two Active Directory authentication methods are supported by Cisco ISE? (Choose two.)',
        ['PPTP',
         'EAP-PEAP',
         'PPP'],
        'MS-CHAPv2',
        'PEAP'),
    QA('Which statement about a distributed Cisco ISE deployment is true?',
        ['It can support up to three load-balanced Administration ISE nodes.',
         'Policy Service ISE nodes can be configured in a redundant failover configuration.',
         'The Active Directory servers of Cisco ISE can be configured in a load-balanced configuration.'],
        'It can support up to two monitoring Cisco ISE nodes for high availability.'),
    QA('Which Cisco ISE feature can differentiate a corporate endpoint from a personal device?',
        ['PAC files',
         'authenticated in-band provisioning',
         'machine authentication'],
        'EAP chaining'),
    QA('Which configuration must you perform on a switch to deploy Cisco ISE in low-impact mode?',
        ['Configure DHCP snooping globally.',
         'Configure IP-device tracking.',
         'Configure BPDU filtering.'],
        'Configure an ingress port ACL on the switchport.'),
    QA('Which profiling capability allows you to gather and forward network packets to an analyzer?',
        ['spanner',
         'retriever',
         'aggregator'],
        'collector'),
    QA('Which network access device feature can you configure to gather raw endpoint data?',
        ['Device Classifier',
         'Switched Port Analyzer',
         'Trust Anchor'],
        'Device Sensor'),
    QA('Which method does Cisco prefer to securely deploy guest wireless access in a BYOD implementation?',
        ['configuring a guest SSID with WPA2 Enterprise authentication',
         'configuring guest wireless users to obtain DHCP centrally from the corporate DHCP server',
         'disabling guest SSID broadcasting'],
        'deploying a dedicated Wireless LAN Controller in a DMZ'),
    QA('Which mechanism does Cisco ISE use to force a device off the network if it is reported lost or stolen?',
        ['dynamic ACLs',
         'SGACL',
         'certificate revocation'],
        'CoA'),
    QA('You discover that the Cisco ISE is failing to connect to the Active Directory server. Which option is a possible cause of the problem?',
        ['There is a certificate mismatch between Cisco ISE and Active Directory.',
         'NAT statements required for Active Directory are configured incorrectly.',
         'The RADIUS authentication ports are being blocked by the firewall.'],
        'NTP server time synchronization is configured incorrectly.'),
    QA('Which type of remediation does Windows Server Update Services provide?',
        ['administrator-initiated remediation',
         'redirect remediation',
         'central Web auth remediation'],
        'automatic remediation'),
    QA('Which three remediation actions are supported by the Web Agent for Windows? (Choose three.)',
        ['Message text',
         'AV definition update',
         'Launch Program'],
        'Automatic Remediation',
        'URL Link',
        'File Distribution'),
    QA('What endpoint operating system provides native support for the SPW?',
        ['Android OS',
         'Windows 8',
         'Mac OS X'],
        'Apple iOS'),
    QA('Which condition triggers wireless authentication?',
        ['Framed-Compression is set to None.',
         'Service-Type is set to Framed.',
         'Tunnel-Type is set to VLAN.'],
        'NAS-Port-Type is set to IEEE 802.11.'),
    QA('Which feature enables the Cisco ISE DHCP profiling capabilities to determine and enforce authorization policies on mobile devices?',
        ['DHCP option 42',
         'DHCP snooping',
         'DHCP spoofing'],
        'disabling the DHCP proxy option'),
    QA('With which two appliance-based products can Cisco Prime Infrastructure integrate to perform centralized management? (Choose two.)',
        ['Cisco Email Security Appliance',
         'Cisco Wireless Location Appliance',
         'Cisco Content Security Appliance'],
        'Cisco Mobility Services Engine',
        'Cisco ISE'),
    QA('Which two options are EAP methods supported by Cisco ISE? (Choose two.)',
        ['EAP-MS-CHAPv2', 'EAP-GTC'],
        'EAP-FAST', 'EAP-TLS'),
    QA('You configured wired 802.1X with EAP-TLS on Windows machines. The ISE authentication detail report shows "EAP-TLS failed SSL/TLS handshake because of an unknown CA in the client certificates chain." What is the most likely cause of this error?',
        ['The Wireless LAN Controller is missing a CA certificate.',
         'The switch is missing a CA certificate.',
         'The Windows Active Directory server is missing a CA certificate.'],
        'The ISE certificate store is missing a CA certificate.'),
    QA('What type of identity group is the Blacklist identity group?',
        ['user',
         'blackhole',
         'quarantine',
         'denied systems'],
        'endpoint'),
    QA('Which feature must you configure on a switch to allow it to redirect wired endpoints to Cisco ISE?',
        ['RADIUS Attribute 29',
         'the RADIUS VSA for accounting',
         'the RADIUS VSA for URL-REDIRECT'],
        'the http secure-server command'),
    QA('In this simulation, you are task to examine the various authentication events using the ISE GUI. For example, you should see events like Authentication succeeded. Authentication failed and etc...\n'
        'Which four statements are correct regarding the event that occurred at 2014-05-07 00:19:07.004? (Choose four.)',
        ['The IT_Corp authorization profile were applied.',
         'The it1 user was authenticated using MAB.',
         'The it1 user machine has passed all the posture assessement tests.'],
        'The it1 user was matched to the IT_Corp authorization policy.',
        'The it1 user supplicant used the PEAP (EAP-MSCHAPv2) authentication method.',
        'The it1 user was successfully authenticated against AD1 identity store.',
        'The it1 user machine has been profiled as a Microsoft-Workstation.'),
    QA('In this simulation, you are task to examine the various authentication events using the ISE GUI. For example, you should see events like Authentication succeeded. Authentication failed and etc...\n'
        'Which three statements are correct regarding the events with the 20 repeat count that occurred at 2014-05-07 00:22:48.748? (Choose three.)',
        ['The device was successfully authenticated using MAB.',
         'The Print Servers authorization profile were applied.',
         'The device is connected to the Gi0/1 switch port and the switch IP address is 10.10.2.2.'],
        'The device matched the Machine_Corp authorization policy.',
        'The device was profiled as a Linksys-PrintServer.',
        'The device MAC address is 00:14:BF:70:B5:FB.'),
    QA('In this simulation, you are task to examine the various authentication events using the ISE GUI. For example, you should see events like Authentication succeeded. Authentication failed and etc...\n'
        'Which two statements are correct regarding the event that occurred at 2014-05-07 00:22:48.175? (Choose two.)',
        ['The DACL will permit http traffic from any host to 10.10.3.20',
         'The DACL will permit icmp traffic from any host to 10.10.2.20',
         'The DACL will permit icmp traffic from any host to 10.10.3.20'],
        'The DACL will permit http traffic from any host to 10.10.2.20',
        'The DACL will permit https traffic from any host to 10.10.3.20'),
    QA('In this simulation, you are task to examine the various authentication events using the ISE GUI. For example, you should see events like Authentication succeeded. Authentication failed and etc...\n'
        'Which two statements are correct regarding the event that occurred at 2014-05-07 00:16:55.393? (Choose two.)',
        ['The failure reason was user entered the wrong username.',
         'The supplicant used the PAP authentication method.',
         'The user was authenticated against the Active Directory then also against the ISE interal user database and both fails.',
         'The NAS switch port where the user connected to has a MAC address of 44:03:A7:62:41:7F',
         'The user failed the MAB.',
         'The supplicant stopped responding to ISE which caused the failure.'],
        'The username entered was it1.',
        'The user is being authenticated using 802.1X.'),
    QA('What are two actions that can occur when an 802.1X-enabled port enters violation mode? (Choose two.)',
        ['The port generates a port resistance error.',
         'The port is prevented from authenticating indefinitely.',
         'The port is placed in quarantine state.',
         'The port attempts to repair the violation.'],
        'The port is error disabled.',
        'The port drops packets from any new device that sends traffic to the port.'),
    QA('In a Cisco ISE deployment, which traffic is permitted by the default dynamic ACL?',
        ['UPD traffic only',
         'management traffic only',
         'TCP traffic only'],
        'all IP traffic'),
    QA('Which two posture redirect ACLs and remediation DACLs must be pushed from Cisco ISE to a Cisco IOS switch if the endpoint must remediate itself? The ISE IP address is 10.201.228.76 and the IP address of the remediating server is 10.201.229.1. (Choose two.)',
        ['ip access-l ex ACL-POSTURE-REDIRECT deny udp any any eq domain deny ip any host 10.201.228.76 permit tcp any any eq 80 permit tcp any any eq 443',
         'POSTURE-REMEDIATION DACL permit udp any any eq domain deny tcp any host 10.201.228.76 permit tcp any any eq 80 permit tcp any any eq 443 permit ip any host 10.210.229.1',
         'POSTURE-REMEDIATION DACL permit udp any any eq domain deny tcp any host 10.201.228.76 deny ip any host 10.210.229.1 permit tcp any any eq 80 permit tcp any any eq 443',
         'ip access-l ex ACL-POSTURE-REDIRECT deny upd any any eq domain permit ip any host 10.201.228.76 permit ip any host 10.201.229.1'],
        'POSTURE-REMEDIATION DACL permit udp any any eq domain permit tcp any host 10.201.228.76 permit tcp any any eq 80 permit tcp any any eq 443',
        'ip access-l ex ACL-POSTURE-REDIRECT deny udp any any eq domain deny ip any host 10.201.228.76 deny ip any host 10.210.229.1 permit tcp any any eq 80 permit tcp any any eq 443'),
    QA('Which statement about the CAK is true?',
        ['It is the key that is used to discover MACsec peers and perform key negotiation between the peers.',
         'It is the key that is used to negotiate session encryption keys.',
         'It is the secret key that encrypts traffic during the connection.',
         'Failed MACsec connections fail back to MAB by default.'],
        'It is the master key that generates the other keys that MACsec requires.'),
    QA('Which devices support download of environmental data and IP from Cisco ISE to STG binding in their SGFW implementation?',
        ['Cisco ISR G3 devices with ZBFW',
         'Cisco ASR devices with ZBFW',
         'Cisco ISR G2 and later devices with ZBFW'],
        'Cisco ASA devices'),
    QA('Which remediation type ensures that Automatic Updates configuration is turned on Windows clients to remediate Windows clients for posture compliance?',
        ['Windows Server Update Services Remediation',
         'Launch Program Remediation',
         'File Remediation',
         'AS Remediation'],
        'Windows Update Remediation'),
    QA('In Cisco ISE 1.3, where is BYOD enabled with dual-SSID onboarding?',
        ['BYOD portal',
         'client provisioning policy',
         'client provisioning resources'],
        'guest portal'),
    QA('Which components must be selected for a client provisioning policy to do a Posture check on the Cisco ISE?',
        ['Configuration Wizard, Wizard Profile',
         'Operating System, Posture Requirements',
         'Remediation Actions, Posture Requirements'],
        'Agent, Profile, Compliance Module'),
    QA('During BYOD flow, where does a Microsoft Windows 8.1 PC download the Network Setup Assistant from?',
        ['from Microsoft App Store',
         'It uses the native OTA functionality',
         'from Cisco App Store'],
        'from Cisco ISE directly'),
    QA('Which ISE feature is used to facilitate a BYOD deployment?',
        ['Local Web Auth',
         'Guest Identity Source Sequence',
         'Guest Service Sponsor Portal'],
        'self-service personal device registration and onboarding'),
    QA('Which 802.1X command ignores Access-Reject during EAP authentication?',
        ['authentication host-mode multi-domain',
         'dot1x pae authenticator',
         'authentication port-control auto',
         'switchport mode access'],
        'authentication open'),
    QA('Which attribute is needed for Cisco ISE to profile a device with HTTP probe?',
        ['sysDescr',
         'OUI',
         'cdp-cache-platform',
         'host-name',
         'dhcp-class-identifier'],
        'user agent'),
    QA('Which configuration is required in the Cisco ISE Authentication policy to allow Central Web Authentication?',
        ['Dot1x and if authentication failed continue',
         'Dot1x and if user not found continue',
         'MAB and if authentication failed continue'],
        'MAB and if user not found continue'),
    QA('Which option is the correct redirect-ACL for Wired-CWA, with 10.201.228.76 being the Cisco ISE IP address?',
        ['ip access-l ACL-WEBAUTH-REDIRECT\n'
         'permit udp any any eq domain\n'
         'permit ip any host 10.201.228.76\n'
         'deny tcp any any eq 80\n'
         'permit tcp any any eq 443',
         'ip access-l ACL-WEBAUTH-REDIRECT\n'
         'permit udp any any eq domain\n'
         'deny ip any host 10.201.228.76\n'
         'permit tcp any any eq 80\n'
         'permit tcp any any eq 443',
         'ip access-l ACL-WEBAUTH-REDIRECT\n'
         'deny udp any any eq domain\n'
         'permit tcp any host 10.201.228.76 eq 8443\n'
         'deny ip any host 10.201.228.76\n'
         'permit tcp any any eq 80'],
        'ip access-l ACL-WEBAUTH-REDIRECT\n'
        'deny udp any any eq domain\n'
        'deny ip any host 10.201.228.76\n'
        'permit tcp any any eq 80\n'
        'permit tcp any any eq 443'),
    QA('How many bits are in a security group tag?',
        ['64', '8', '32'], '16'),
    QA('Which option is the correct format of username in MAB authentication?',
        ['CISCO/chris', 'chris@cisco.com', 'host/LSB67.cisco.com'],
        '10:41:7F:46:9F:89'),
    QA('Which description of the purpose of the continue option in an authentication policy rule is true?',
        ['It sends an authentication to the next subrule within the same authentication rule.',
         'It sends an authentication to the selected identity store.',
         'It causes Cisco ISE to ignore the NAD because NAD will treat the Cisco ISE server as dead.',
         'It allows Cisco ISE to check the list of rules in an authentication policy until there is a match.'],
        'It allows Cisco ISE to proceed to the authorization policy regardless of authentication pass/fail.'),
    QA('If the user matches the given TACACS+ profile on Cisco ISE, which command can the user enter from shell prompt on a Cisco switch?',
        ['enable', 'show run', 'configure terminal'], 'enable 10'),
    QA('Which option describes the purpose of configuring Native Supplicant Profile on the Cisco ISE?',
        ['It provides posture assessments and remediation for devices that are attempting to gain access to the corporate network.',
         'It helps employees add and manage new devices by entering the MAC address for the device.',
         'It is used to register personal devices on the network.'],
        'It enforces the use of MSCHAPv2 or EAP-TLS for 802.1X authentication.'),
    QA('A user configured a Cisco Identity Service Engine and switch to work with downloadable access list for wired dot1x users, though it is failing to work.\n'
        'Which command must be added to address the issue?',
        ['dot1x pae authenticator',
         'aaa authentication dot1x default group radius',
         'ip dhcp snooping'],
        'ip device tracking'),
    QA('If a user with privilege 15 is matching this command set on Cisco ISE 2.0, which three commands can the user execute? (Choose three.)',
        ['ping 10.10.100.1', 'exit', 'show clock'],
        'show run', 'show ip interface brief', 'configure terminal'),
    QA('Which two options must be used on Cisco ISE to enable the TACACS+ feature? (Choose two.)',
        ['TACACS Command Sets',
         'TACACS External Servers',
         'TACACS Profiles',
         'TACACS Server Sequence',
         'TACACS+ Authentication Settings'],
        'Device Administration License',
        'Enable Device Admin Service'),
    QA('How many days does Cisco ISE wait before it purges a session from active session list if no RADIUS Accounting STOP message is received?',
        ['15', '1', '10'], '5'),
    QA('Which two attributes are delivered by the DHCP probe to the Cisco ISE? (Choose two.)',
        ['MAC address',
         'calling-station-ID',
         'framed-IP-address'],
        'host-name',
        'dhcp-client-identifier'),
    QA('Which command on the switch ensures that the Service-Type attribute is sent with all Radius authentication request?',
        ['radius-server attribute 25 access-request include',
         'radius-server attribute 31 send nas-port-detail',
         'radius-server attribute 8 include-in-access-req'],
        'radius-server attribute 6 on-for-login-auth'),
    QA('Which profiling probe collects the user-agent string?',
        ['Network Scan', 'NetFlow', 'DHCP'], 'HTTP'),
    QA('By default, how many days does Cisco ISE wait before it purges the expired guest accounts?',
        ['10', '1', '20'], '15'),
    QA('Which redirect-URL is pushed by Cisco ISE for posture redirect for corporate users?',
        ['https://ise1.cisco.com:8443/portal/gateway?sessionId=0A00023D0000003A239F78CC&portal=283258a0-e96e-11e4-a30a- 005056bf01c9&action=drw&token=a1a6ea71ea8f410c2637e11ba534379e',
         'https://ise1.cisco.com:8443/portal/gateway?sessionId=0A00023D0000003A239F78CC&portal=283258a0-e96e-11e4-a30a- 005056bf01c9&action=mdm&token=a1a6ea71ea8f410c2637e11ba534379e',
         'https://ise1.cisco.com:8443/portal/gateway?sessionId=0A00023D0000003A239F78CC&portal=283258a0-e96e-11e4-a30a- 005056bf01c9&action=cwa&token=a1a6ea71ea8f410c2637e11ba534379e'],
        'https://ise1.cisco.com:8443/portal/gateway?sessionId=0A00023D0000003A239F78CC&portal=283258a0-e96e-11e4-a30a- 005056bf01c9&action=cpp&token=a1a6ea71ea8f410c2637e11ba534379e'),
    QA('Which operating system type needs access to the Internet to download the application that is required for BYOD on-boarding?',
        ['OSX', 'iOS', 'Windows'], 'Android'),
    QA('In a distributed deployment of Cisco ISE, which column in Figure 1 is used to fill in the Host Name field in Figure 2 to collect captures on Cisco ISE while authenticating the specific endpoint?',
        ['Identity', 'Network Device', 'Endpoint ID'], 'Server'),
    QA('Which two options can a sponsor select to create bulk guest accounts from the sponsor portal? (Choose two.)',
        ['Yearly', 'Daily', 'Known', 'Monthly'], 'Imported', 'Random'),
    QA('Which two things must be verified if authentication is failing with this error message? (Choose two.)',
        ['Cisco ISE HTTPS/admin certificate is valid.',
         'CA cert chain of the client certificate is installed on Cisco ISE.',
         'Cisco ISE server certificate is installed on the client.'],
        'Cisco ISE EAP identity certificate is valid.',
        'CA cert chain of Cisco ISE EAP certificate is installed on the trusted certs store of the client machine.'),
    QA('Which option is one method for transporting security group tags throughout the network?',
        ['by embedding the SGT in the IP header',
         'by enabling 802.1AE on every network device',
         'by embedding the SGT in the 802.1Q header'],
        'via Security Group Exchange Protocol'),
    QA('In Cisco ISE 1.3 and above, which two operations are allowed on Endpoint Certificates pages for issued endpoint certificates on the admin portal? (Choose two.)',
        ['delete',
         'unrevoke',
         'export'],
        'revoke',
        'view'),
    QA('In Cisco 1.3, which feature is available to a sponsor in a sponsor group?',
        ['Allow the user to download a native supplicant profile.',
         'Help employees add and manage new devices by entering the MAC address for the device.',
         'Reinstate or delete devices that were registered previously.'],
        'Restrict sponsors from viewing guest passwords.'),
    QA('An engineer is troubleshooting an issue between the switch and the Cisco ISE where the 802.1X and MAB authentication and authorization are successful. Which command does the network engineer enter on the switch to troubleshoot this issue and look for active sessions?',
        ['Show emp session summary',
         'Show dot1x all',
         'Show connections detail'],
        'Show authentication sessions'),
    QA('Which two accounting types are used to implement accounting with RADIUS? (Choose two.)',
        ['User', 'Attribute', 'Device'], 'Network', 'Resource'),
    QA('Which type of SGT propagation does a WLC in a data center require?',
        ['SGT', 'SGT inline', 'SGT Reflector'], 'SXP'),
    QA('A user reports that a switchs RADIUS accounting packets are not being seen on the Cisco ISE server. Which command is the user missing in the switchs configuration?',
        ['aaa accounting exec default start-stop group radius',
         'aaa accounting network default start-stop group radius',
         'aaa accounting resource default start-stop group radius'],
        'radius-server vsa send accounting'),
    QA('Which three options can be pushed from a Cisco ISE server as part of a successful 802.1X authentication? (Choose three.)',
        ['Posture status', 'Authentication priority', 'Authentication order'],
        'Reauthentication timer', 'DACL', 'VLAN'),
    QA('What are the four code fields which identify the type of an EAP packet?',
        ['Request, Reply, Success, Failure',
         'Request, Response, Accept, Reject',
         'Request, Reply, Accept, Reject'],
        'Request, Response, Success, Failure'),
    QA('Which port does Cisco ISE use for native supplicant provisioning of a Windows machine?',
        ['TCP/UDP 8905', 'TCP 443', 'TCP 8443'], 'TCP/UDP 8909'),
    QA('If the host sends a packet across the Cisco TrustSec domain, where is the SGACL enforced?',
        ['Dynamically at the host',
         'After the packet enters the Cisco TrustSec domain',
         'At the ingress router.'],
        'At the egress router'),
    QA('Which Smart Call Home profile is used for anonymous reporting?',
        ['Admin-1', 'Isesch-1', 'Anon-1'], 'Ciscotac-1'),
    QA('An engineer must limit the configuration parameters that can be executed on the Cisco ASAs deployed throughout the network. Which command allows the engineer to complete this task?',
        ['AAA-server tacacs1(inside) host 10.5.109.18 $3cr37 timeout2 ! aaa authentication ssh console tacacs1',
         'AAA-server tacacs1(inside) host 10.5.109.18 $3cr37 timeout2 ! aaa authorization exec authentication-server',
         'AAA-server tacacs1(inside) host 10.5.109.18 $3cr37 timeout2 ! aaa authentication exclude ssh'],
        'AAA-server tacacs1(inside) host 10.5.109.18 $3cr37 timeout2 ! aaa authorization command tacacs1'),
    QA('An engineer is designing a BYOD environment utilizing Cisco ISE for devices that do not support native supplicants. Which portals must the security engineer configure to accomplish this task?',
        ['Client Provisioning Portals',
         'BYOD Portals',
         'MDM Portals'],
        'My Devices Portals'),
    QA('Which two protocols does Cisco Prime Infrastructure use for device discovery? (Choose two.)',
        ['SNAP', 'RARP', 'LACP'], 'LLDP', 'DNS'),
    QA('Which ISE flow mode does this diagram represent?',
        ['Closed mode', 'Application mode', 'Low-impact mode'], 'Monitor mode'),
    QA('How does the device sensor send information to a RADIUS server?',
        ['Analyzer', 'Authorization', 'Collector'], 'Accounting'),
    QA('What two values does Cisco recommend you adjust and test to set the optimal timeout value for your network’s specific 802.1X MAB deployment? (Choose two.)',
        ['Supp-timeout', 'Max-req', 'Server-timeout'],
        'Max-reath-req', 'Tx-period'),
    QA('Which RADIUS attribute can be used to dynamically assign the inactivity active timer for MAB users from Cisco ISE node?',
        ['Session-timeout attribute',
         'Radius-server timeout',
         'Termination-action attribute'],
        'Idle-timeout attribute'),
    QA('Which two additional fields are added to an Ethernet frame when implementing MACsec? (Choose two.)',
        ['Encapsulating security payload',
         'Authentication host mode',
         'Authentication header'],
        'Security tag',
        'Message authentication code'),
    QA('Which packets are allowed on a dot1x port with no authentication open before the port goes to an authorized state?',
        ['DHCP, EAPOL, HTTP',
         'CDP, DHCP, DNS',
         'CDP, EAPOL, HTTP'],
        'CDP, EAPOL, STP'),
    QA('An engineer must enable SGACL policy globally for a Cisco TrustSec –enabled routed interface. Which command must be used?',
        ['cts role-based monitor enable',
         'cts role-based sgt-caching with-enforcement',
         'cts role-based monitor permissions from {sgt_num} to {dgt_num}][ipv4| ipv6]'],
        'cts role-based enfrocement'),
    QA('Which statement about the authentication protocol used in the configuration is true?',
        ['The authentication request contains only a username.',
         'The authentication request contains only a password.',
         'There is separate authentication and authorization request packet.'],
        'The authentication and authorization requests are grouped in a single packet.'),
    QA('A company has implemented a dual SSID BYOD design. A provisioning SSID is used for user registration, and an employee SSID is used for company network access. Which controller option must be enabled to allow a user to switch immediately from the provisioning SSID to the employee SSID after registration has been completed?',
        ['AAA override', 'User Idle Timeout' 'AP Fallback'],
        'Fast SSID Change'),
    QA('Which two options are functional components of the posture service? (Choose two.)',
        ['Quarantined policy',
         'Secure policy',
         'Network provisioning'],
        'Posture policy',
        'Client provisioning'),
    QA('A company has implemented a dual SSID BYOD design. A provisioning SSID is used for user registration, and an employee SSID is used for company network access. How is the layer 2 security of the provisioning SSID configured?',
        ['802.1x',
         'WPA2',
         'MAC filtering disabled'],
        'Open'),
    QA('A company wants to allow employees to register and manage their own devices that do not support NSP. Which portals enable this ability?',
        ['Client Provisioning Portals',
         'BYOD Portals',
         'MDM Portals'],
        'My Device Portals'),
    QA('Which definition of "posturing" as it relates to a general network infrastructure and access into the internal network is true?',
        ['The process by which an end device can be monitored while connected to the network to determine if it could contain possible viruses or potential harmful programs running.',
         'The process by which an operating system or application running on an endpoint provides critical information about the internet activity being used by an endpoint.',
         'The process by which an operating system or application running on an endpoint provides critical information about the software that is actively running on the device.'],
        'The process when software is uploaded to an end device before it is allowed to gain access to a secure network.'),
    QA('A customer is concerned with the use of the issued laptops even when devices are not on the corporate network. Which agent continues to be operational even when the host is not on the Cisco ISE network?',
        ['Cisco ISE Agent',
         'Cisco Custom Agent',
         'Cisco NAC Web Agent'],
        'Cisco NAC Agent'),
    QA('Which three ISE posture remediation actions are supported by the Web Agent for Windows? (Choose three.)',
        ['Automatic Remediation',
         'AV definition update',
         'Launch program'],
        'URL Link',
        'Message text',
        'File Distribution'),
    QA('What are three portals provided by PSN? (Choose three.)',
        ['Monitoring',
         'Troubleshooting',
         'Admin'],
        'Sponsor',
        'Guest',
        'My devices'),
    QA('An engineer is investigating an issue with their Posture Run-time Services implementation. Which protocol services are used by NAC Agents to communicate with NAC Servers?',
        ['IPSec', 'IKEv2', 'Fix'], 'SWISS'),
    QA('Which statement describes this switch configuration?',
        ['802.1x is disabled on the switch port and all traffic is allowed as normal without restriction.',
         'The switch port begins in the unauthorized state and does not allow EAPOL, Cisco Discovery Protocol, and STP traffic.',
         '802.1x is enabled on the switch port and the switch port ignores all traffic.'],
        'The switch port begins in the unauthorized state and allows only EAPOL, Cisco Discovery Protocol, and STP traffic.'),
    QA('Which option is a recommended agent for guest posture assessment?',
        ['Mac OSX Agent',
         'Mac OSX Web Agent',
         'Windows NAC Agent'],
        'Windows Web Agent'),
    QA('When using endpoint access control, which two access methods are valid for authentication and authorization? (Choose two.)',
        ['Microsoft Challenge Handshake Authentication',
         'Protected extensible authentication',
         'Password Authentication Protocol Bypass'],
        'MAC Authentication Bypass',
        'Web authentication'),
    QA('Which type of SGT classification method is required when authentication is unavailable?',
        ['Bypass',
         'Dynamic',
         'Inline'],
        'Static'),
    QA('A network is seeing a posture status "unknown" for a single corporate machine on the Cisco ISE authentication report, whereas the other machines and reported as "complaint". Which option is the reason for machine being reported as "unknown"?',
        ['Posture compliance condition is missing on the machine.',
         'Posture service is disabled on Cisco ISE.',
         'Posture policy does not support the OS.'],
        'Posture agent is not installed on the machine.'),
    QA('Which ISE deployment mode is similar to the industry standard 802.1X behavior?',
        ['Monitor mode',
         'Low-impact mode',
         'Policy mode'],
        'Closed mode'),
    QA('Within a BYOD environment, when employees add devices using the My Devices Portal, which identity Group does Cisco ISE assign the endpoints to?',
        ['Profiled',
         'Employee',
         'Guest'],
        'Registered'),
    QA('When using CA for identity source, which method can be used to provide real-time certificate validation?',
        ['X.509', 'PKI', 'OCSP'], 'CRL'),
    QA('An engineer of Company A will be sending guest credentials through SMS to conference participants. Which portal must the engineer use for this task?',
        ['Sponsor', 'User', 'Guest'], 'SMS'),
    QA('An engineer of Company A wants to know what kind of devices are connecting to the work. Which service can be enabled on the Cisco ISE node?',
        ['MAB',
         'Central web authentication',
         'Profiling'],
        'Posture'),
    QA('Which supplicants(s) and server(s) are capable of supporting EAP-CHAINING?',
        ['Cisco AnyConnect NAM and Cisco Access Control Server',
         'Cisco Secure Services Client and Cisco Access Control Server',
         'Windows Native Supplicant and Cisco Identity Service Engine'],
        'Cisco AnyConnect NAM and Cisco Identity Service Engine'),
    QA('Which advanced option within a WLAN must be enabled to trigger Central Web Authentication for wireless users?',
        ['Static IP tunneling',
         'Diagnostic channel',
         'DHCP server'],
        'AAA override'),
    QA('When using a DHCP probe in a Cisco ISE deployment, which type of request triggers an endpoint to be reprofiled?',
        ['RENEWING',
         'REBINDING',
         'DHCPInform'],
        'INIT-REBOOT'),
    QA('Which description of the use of low-impact mode in a Cisco ISE deployment is correct?',
        ['Low-impact mode must be the final phase in deploying Cisco ISE into a network environment using the phased approach.',
         'The port does not allow any traffic before the authentication (except for EAP, Cisco Discovery Protocol, and LLDP), and then the port is assigned to specific authorization results after the authentication.',
         'It enables authentication (with authentication open), sees exactly which devices fail and which succeed, and corrects the failed authentications before they cause any problems.'],
        'It continues to use the authentication open capabilities of the switch port, which allows traffic to enter the switch before an authentication result.'),
    QA('In this simulation, you will need to answer three multiple choice questions by examining the current ISE configurations using the ISE GUI.\n'
        'To access the ISE GUI, click on the ISE icon in the topology diagram to access the ISE GUI.\n'
        'Not all the ISE GUI screen are operational in this simulation and some of the ISE GUI operations have been reduced in this simulation.\n'
        'Not all the links on each of the ISE GUI screen works, if some of the links are not working on a screen, click Home to go back to the Home page first. From the Home page, you can access all the required screens.\n'
        'To view some larger GUI screens, use the simulation window scroll bars. Some of the larger GUI screens only shows partially but will include all information required to complete this simulation.\n\n'
        'What are two possible reasons why many Sales and IT users are unable to authenticate and access the network using their AnyConnected NAM client and EAP-FAST? (Choose two.)',
        ['The IP-Corp authorization profile has the wrong Access Type configured.',
         'The authorization profile used for the Sales users is misconfigured.',
         'Many of the IT Sales and IT user machines are not passing the ISE posture assessment.',
         'The PERMIT_ALL_TRAFFIC DACL is missing the permit ip any any statements in the end.',
         'The Employee_FullAccess_DACL DACL is missing the permit ip any any statement in the end.'],
        'The Dot1X authentication policy is not allowing the EAP-FAST protocol.',
        'The order for the MAB authentication policy and the Dot1X authentication policy should be reversed.'),
    QA('In this simulation, you will need to answer three multiple choice questions by examining the current ISE configurations using the ISE GUI.\n'
        'To access the ISE GUI, click on the ISE icon in the topology diagram to access the ISE GUI.\n'
        'Not all the ISE GUI screen are operational in this simulation and some of the ISE GUI operations have been reduced in this simulation.\n'
        'Not all the links on each of the ISE GUI screen works, if some of the links are not working on a screen, click Home to go back to the Home page first. From the Home page, you can access all the required screens.\n'
        'To view some larger GUI screens, use the simulation window scroll bars. Some of the larger GUI screens only shows partially but will include all information required to complete this simulation.\n\n'
        'Which statement is true?',
        ['Currently, IT users who successfully authenticate will have their packets tagged with s SGT of 3.',
         'Currently, IT users who successfully authenticate will be assigned to VLAN 9.',
         'Currently, any domain administrator who successfully authenticate will be assigned to VLAN 10.',
         'Print Servers matching the Linksys-PrintServer identity group will have the following access restrictions: permit icmp any host 10.10.2.20 permit tcp any host 10.10.2.20 eq 80 permit icmp any host 10.10.3.20 permit tcp any host 10.10.3.20 eq 80'],
        'Computers belonging to the secure-x domain which passes machine authentication but failed user authentication will have the Employee_Restricted_DACL applied.'),
    QA('Which two statements are true? (Choose two.)',
        ['The ISE is not able to successfully connect to the hq-srv.secure-x.local AD server.',
         'The ISE internal user database has two accounts enabled: student and test that maps to the Employee user identify group.'],
        'The ISE internal endpoints database is used authenticate any users not in the Active Directory domain.',
        'Guest_Portal_Sequence is a built-in identity source sequence.'),
]

corrCount = 0
qnumber = 1
random.shuffle(qaList)

for qaItem in qaList[:60]:
    print(f'Question {qnumber}\n' + qaItem.question)
    if qaItem.corrAnsw5 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + [qaItem.corrAnsw3] + \
            [qaItem.corrAnsw4] + [qaItem.corrAnsw5]
    elif qaItem.corrAnsw4 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + \
            [qaItem.corrAnsw3] + [qaItem.corrAnsw4]
    elif qaItem.corrAnsw3 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + [qaItem.corrAnsw3]
    elif qaItem.corrAnsw2 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2]
    else:
        possible = qaItem.otherAnsw + [qaItem.corrAnsw]
    random.shuffle(possible)
    count = 0    # list indexes start at 0 in python
    while count < len(possible):
        print(str(count + 1) + ': ' + possible[count])
        count += 1

    if qaItem.corrAnsw5 is not None:
        print('Please enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        print('Please enter the number of your fourth answer:')
        userAnsw4 = input()
        while not userAnsw4.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw4 = input()
        userAnsw4 = int(userAnsw4)
        print('Please enter the number of your fifth answer:')
        userAnsw5 = input()
        while not userAnsw5.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw5 = input()
        userAnsw5 = int(userAnsw5)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or possible[userAnsw - 1] == qaItem.corrAnsw2 or possible[userAnsw - 1] == qaItem.corrAnsw3 or possible[userAnsw - 1] == qaItem.corrAnsw4 or possible[userAnsw - 1] == qaItem.corrAnsw5) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or possible[userAnsw2 - 1] == qaItem.corrAnsw2 or possible[userAnsw2 - 1] == qaItem.corrAnsw3 or possible[userAnsw2 - 1] == qaItem.corrAnsw4 or possible[userAnsw2 - 1] == qaItem.corrAnsw5) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or possible[userAnsw3 - 1] == qaItem.corrAnsw2 or possible[userAnsw3 - 1] == qaItem.corrAnsw3 or possible[userAnsw3 - 1] == qaItem.corrAnsw4 or possible[userAnsw3 - 1] == qaItem.corrAnsw5) and \
            (possible[userAnsw4 - 1] == qaItem.corrAnsw or possible[userAnsw4 - 1] == qaItem.corrAnsw2 or possible[userAnsw4 - 1] == qaItem.corrAnsw3 or possible[userAnsw4 - 1] == qaItem.corrAnsw4 or possible[userAnsw4 - 1] == qaItem.corrAnsw5) and \
                (possible[userAnsw5 - 1] == qaItem.corrAnsw or possible[userAnsw5 - 1] == qaItem.corrAnsw2 or possible[userAnsw5 - 1] == qaItem.corrAnsw3 or possible[userAnsw5 - 1] == qaItem.corrAnsw4 or possible[userAnsw5 - 1] == qaItem.corrAnsw5):
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(
                f'Correct answer was: {qaItem.corrAnsw}, {qaItem.corrAnsw2}, '
                f'{qaItem.corrAnsw3}, {qaItem.corrAnsw4}, '
                f'and {qaItem.corrAnsw5}')
        print('')
    elif qaItem.corrAnsw4 is not None:
        print('Please enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        print('Please enter the number of your fourth answer:')
        userAnsw4 = input()
        while not userAnsw4.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw4 = input()
        userAnsw4 = int(userAnsw4)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or possible[userAnsw - 1] == qaItem.corrAnsw2 or possible[userAnsw - 1] == qaItem.corrAnsw3 or possible[userAnsw - 1] == qaItem.corrAnsw4) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or possible[userAnsw2 - 1] == qaItem.corrAnsw2 or possible[userAnsw2 - 1] == qaItem.corrAnsw3 or possible[userAnsw2 - 1] == qaItem.corrAnsw4) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or possible[userAnsw3 - 1] == qaItem.corrAnsw2 or possible[userAnsw3 - 1] == qaItem.corrAnsw3 or possible[userAnsw3 - 1] == qaItem.corrAnsw4) and \
                (possible[userAnsw4 - 1] == qaItem.corrAnsw or possible[userAnsw4 - 1] == qaItem.corrAnsw2 or possible[userAnsw4 - 1] == qaItem.corrAnsw3 or possible[userAnsw4 - 1] == qaItem.corrAnsw4):
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(
                f'Correct answer was: {qaItem.corrAnsw}, {qaItem.corrAnsw2}, '
                f'{qaItem.corrAnsw3}, and {qaItem.corrAnsw4}')
        print('')
    elif qaItem.corrAnsw3 is not None:
        print('Please enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or possible[userAnsw - 1] == qaItem.corrAnsw2 or possible[userAnsw - 1] == qaItem.corrAnsw3) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or possible[userAnsw2 - 1] == qaItem.corrAnsw2 or possible[userAnsw2 - 1] == qaItem.corrAnsw3) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or possible[userAnsw3 - 1] == qaItem.corrAnsw2 or possible[userAnsw3 - 1] == qaItem.corrAnsw3):
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(
                f'Correct answer was: {qaItem.corrAnsw}, {qaItem.corrAnsw2}, '
                f'and {qaItem.corrAnsw3}')
        print('')
    elif qaItem.corrAnsw2 is not None:
        print('Please enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or possible[userAnsw - 1] == qaItem.corrAnsw2) and \
                (possible[userAnsw2 - 1] == qaItem.corrAnsw or possible[userAnsw2 - 1] == qaItem.corrAnsw2):
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(
                f'Correct answer was: {qaItem.corrAnsw}, '
                f'and {qaItem.corrAnsw2}')
        print('')
    else:
        print('Please enter the number of your answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        if possible[userAnsw - 1] == qaItem.corrAnsw:
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(f'Correct answer was: {qaItem.corrAnsw}')
        print('')
    qnumber += 1

print(f'You answered {corrCount} out of 60 questions correctly.')
print(f'An approximate score of {int(corrCount/60*1000)}')


# SPARE QUESTION
#    QA('Changes were made to the ISE server while troubleshooting, and now all wireless certificate authentications are failing. Logs indicate an EAP failure.\n'
#         'What is the most likely cause of the problem?',
#         ['Certificate authentication profile is not configured in the Identity Store',
#            'MS-CHAPv2-is not checked in the Allowed Protocols list',
#            'Default rule denies all traffic',
#            'Client root certificate is not included in the Certificate '
#            'Store'],
#         'EAP-TLS is not checked in the Allowed Protocols list'),
# QA('Which two things must be verified if authentication is failing with this error message? (Choose two.)',
#     ['Cisco ISE HTTPS/admin certificate is valid.',
#      'CA cert chain of the client certificate is installed on Cisco ISE.',
#      'Cisco ISE server certificate is installed on the client.'],
#     'Cisco ISE EAP identity certificate is valid.',
#     'CA cert chain of Cisco ISE EAP certificate is installed on the trusted certs store of the client machine.'),
