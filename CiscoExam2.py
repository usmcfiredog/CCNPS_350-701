import random
# from PIL import Image


class QA:
    def __init__(self, question, otherAnswers, correctAnswer,
                 correctAnswer2=None, correctAnswer3=None):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAnsw = otherAnswers
        self.corrAnsw2 = correctAnswer2
        self.corrAnsw3 = correctAnswer3


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
       [
           'MACsec in Multiple-Host Mode in order to open or close a port based on a single authentication',
           'Identity-based ACLs on the switches with user identities provided by ISE',
           'Cisco Threat Defense for user group control by leveraging Netflow exported from the switches and login information from ISE'
       ],
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
       ['ASA1(config)# access-list IPX-Allow ethertype permit ipx',
        'ASA1(config)# access-list IPX-Allow ethertype permit ipx ASA1(config)# access-group IPX-Allow in interface outside',
        'ASA1(config)# access-list IPX-Allow ethertype permit ipx ASA1(config)# access-group IPX-Allow in interface inside'],
        'ASA1(config)# access-list IPX-Allow ethertype permit ipx ASA1(config)# access-group IPX-Allow in interface global'),
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
       [
           'It allows the WLC to failover because of congestion.',
           'It enables stations to remain in power-save mode, except at specified intervals to receive data from the access point.'
       ],
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
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),
    QA('',
       ['', '', ''], ''),






]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
    print(qaItem.question)
#   print('Possible answers are:')
    # square brackets turn correct answer into list for concatenating with
    # other list
    if qaItem.corrAnsw3 is not None:
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

    if qaItem.corrAnsw3 is not None:
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
