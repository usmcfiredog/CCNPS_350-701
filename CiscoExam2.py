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
    QA('Changes were made to the ISE server while troubleshooting, and now all wireless certificate authentications are failing. Logs indicate an EAP failure. '
       'What is the most likely cause of the problem?',
       ['Certificate authentication profile is not configured in the Identity Store',
        'MS-CHAPv2-is not checked in the Allowed Protocols list',
        'Default rule denies all traffic',
        'Client root certificate is not included in the Certificate '
        'Store'],
       'EAP-TLS is not checked in the Allowed Protocols list'),
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
       '4. Install the issued certificate on the ISE.'
       ),
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
       'LLDP agent information', 'open ports'),
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
    QA('',
       ['',
        '',
        ''],
       ''),






]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
    print(qaItem.question)
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
    count = 0  # list indexes start at 0 in python
    while count < len(possible):
        print(str(count+1) + ': ' + possible[count])
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
        if possible[userAnsw - 1] == qaItem.corrAnsw and \
            possible[userAnsw2 - 1] == qaItem.corrAnsw2 and \
                possible[userAnsw3 - 1] == qaItem.corrAnsw3 and \
            possible[userAnsw4 - 1] == qaItem.corrAnsw4 and \
            possible[userAnsw5 - 1] == qaItem.corrAnsw5:
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
        if possible[userAnsw - 1] == qaItem.corrAnsw and \
            possible[userAnsw2 - 1] == qaItem.corrAnsw2 and \
                possible[userAnsw3 - 1] == qaItem.corrAnsw3 and \
            possible[userAnsw4 - 1] == qaItem.corrAnsw4:
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
        if possible[userAnsw - 1] == qaItem.corrAnsw and \
            possible[userAnsw2 - 1] == qaItem.corrAnsw2 and \
                possible[userAnsw3-1] == qaItem.corrAnsw3:
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
        if possible[userAnsw - 1] == qaItem.corrAnsw and \
                possible[userAnsw2-1] == qaItem.corrAnsw2:
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(
                f'Correct answer was: {qaItem.corrAnsw}, '
                f'and {qaItem.corrAnsw2}')
        print('')
    else:
        print('Please enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        if possible[userAnsw-1] == qaItem.corrAnsw:
            print('Your answer was correct.')
            corrCount += 1
        else:
            print('Your answer was wrong.')
            print(f'Correct answer was: {qaItem.corrAnsw}')
        print('')

print('You answered ' + str(corrCount) + ' of ' +
      str(len(qaList)) + ' questions correctly.')
