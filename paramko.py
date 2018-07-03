import paramiko as pa

ssh = pa.SSHClient()


ssh.set_missing_host_key_policy(pa.AutoAddPolicy())
ssh.connect('XXXX',port=22,username='pshanmug', password='Krishna16')
print("connected")
stdin,stdout,stderr = ssh.exec_command('ls -l')

output = stdout.readlines()
type(output)
print("\n".join(output))


#-----------------------------
import paramiko

# def test_ssh(self, mock_exec, mock_conn, mock_set):
#     mock_log = mock.Mock()
#     mock_channel = mock.Mock()
#     mock_exec.return_value = (fake_channel_file(['input']),
#                               fake_channel_file(['out_line1',
#                                                  'out_line2'],
#                                                 mock_channel),
#                               fake_channel_file(['err_line1',
#                                                  'err_line2']))
#     mock_channel.recv_exit_status.return_value = 0
#
#     client = sshclient.SSHClient('ehpsalnabit01v.e-hps.com', 22, username='pshanmug', password='Krishna16',
#                                  log=mock_log)
#     out, err = client.ssh('pwd', output=True)
#
#     mock_log.debug.assert_called()
#     mock_exec.assert_called()
#     mock_log.info.assert_called_with('out_line1\nout_line2')
#     mock_log.error.assert_called_with('err_line1\nerr_line2')
#     mock_channel.recv_exit_status.assert_called_with()
#     self.assertEqual(out, 'out_line1\nout_line2')
#     self.assertEqual(err, 'err_line1\nerr_line2')
#     print (mock_log.info)


# nbytes = 4096
# hostname = '192.168.1.26'
# port = 22
# username = 'admin'
# password = '12345'
# command = 'show ip int brief'
#
# client = paramiko.Transport('ehpsalnabit01v.e-hps.com', 22)
# client.connect(username='pshanmug', password='Krishna16')
#
# print("connection made in the ip")


# stdout_data = []
# stderr_data = []
# session = client.open_channel(kind='session')
# session.exec_command(command)
# # while True:
# #     if session.recv_ready():
# #         print("one")
# #         stdout_data.append(session.recv(nbytes))
# #         var= session.recv(nbytes)
# #         var2 = var.decode("utf-8")
# #         print(var)
# #         print(var2)
# #         print("tow")
# #         print(stdout_data)
#
# print(stdout.readlines())
# session.close()
# client.close()


