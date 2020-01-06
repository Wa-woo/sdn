# -*- coding: utf-8 -*-
import httplib2
import time
import json
class OdlUtil:
	url = ''
	def __init__(self, host, port):
		self.url = 'http://' + host + ':' + str(port)
	def install_flow(self, container_name='default',username="admin", password="admin"):
		http = httplib2.Http()
		http.add_credentials(username, password)
		headers = {'Accept': 'application/json'}
		flow_name = 'flow_' + str(int(time.time()*1000))
		#设置s4流表
		#设置h2发往s4的端口1的流表，优先级最高
		h2_to_s4_1 ='{"flow": [{"id": "41","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
            		'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "1"},"order": "0"}]}}]},'\
            		'"priority": "115","cookie": "1","table_id": "0"}]}'
		lh2_to_s4_1 ='{"flow": [{"id": "41","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "2"},"order": "0"}]}}]},'\
            		'"priority": "105","cookie": "1","table_id": "0"}]}'

		#设置h3发往s4的端口1的流表，优先级最高
		h3_to_s4_1 ='{"flow": [{"id": "51","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "1"},"order": "0"}]}}]},'\
            		'"priority": "115","cookie": "1","table_id": "0"}]}'


		#设置h4发往s4的端口1的流表，优先级最高
		h4_to_s4_1 ='{"flow": [{"id": "61","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.4/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "1"},"order": "0"}]}}]},'\
            		'"priority": "115","cookie": "1","table_id": "0"}]}'

		#当s4的端口1流量满载时，h2发的数据包走端口2,3的流表，优先级高	
		h2_to_s4_2 ='{"flow": [{"id": "42","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "2"},"order": "0"}]}}]},'\
            		'"priority": "112","cookie": "1","table_id": "0"}]}'
		h2_to_s4_3 ='{"flow": [{"id": "43","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "3"},"order": "0"}]}}]},'\
            		'"priority": "110","cookie": "1","table_id": "0"}]}'

		#当s4的端口1流量满载时，h3发的数据包走端口2,3的流表，优先级高
		h3_to_s4_2 ='{"flow": [{"id": "52","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "2"},"order": "0"}]}}]},'\
            		'"priority": "112","cookie": "1","table_id": "0"}]}'
		h3_to_s4_3 ='{"flow": [{"id": "53","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "3"},"order": "0"}]}}]},'\
            		'"priority": "110","cookie": "1","table_id": "0"}]}'

		#当s4的端口1流量满载时，h4发的数据包走端口2,3的流表，优先级高
		h4_to_s4_2 ='{"flow": [{"id": "62","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.4/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "2"},"order": "0"}]}}]},'\
            		'"priority": "112","cookie": "1","table_id": "0"}]}'
		h4_to_s4_3 ='{"flow": [{"id": "63","match": {"ethernet-match":'\
               		'{"ethernet-type": {"type": "2048"}},'\
					'"ipv4-source":"10.0.0.4/32","ipv4-destination": "10.0.0.1/32"},'\
            		'"instructions": {"instruction": [{"order": "0",'\
                	'"apply-actions": {"action": [{"output-action": {'\
                	'"output-node-connector": "3"},"order": "0"}]}}]},'\
            		'"priority": "110","cookie": "1","table_id": "0"}]}'

		#s2流表
		s2_2to1='{"flow": [{"id": "1","match": {"ethernet-match":'\
            '{"ethernet-type": {"type": "2048"}},'\
			'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            '"instructions": {"instruction": [{"order": "0",'\
            '"apply-actions": {"action": [{"output-action": {'\
            '"output-node-connector": "1"},"order": "0"}]}}]},'\
            '"priority": "105","cookie": "1","table_id": "0"}]}'
		#s3流表
		s3_2to1='{"flow": [{"id": "1","match": {"ethernet-match":'\
            	'{"ethernet-type": {"type": "2048"}},'\
				'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
            	'"apply-actions": {"action": [{"output-action": {'\
            	'"output-node-connector": "1"},"order": "0"}]}}]},'\
            	'"priority": "105","cookie": "1","table_id": "0"}]}'
		#s1流表
		s1_234to1='{"flow": [{"id": "1","match": {"ethernet-match":'\
            	'{"ethernet-type": {"type": "2048"}},'\
				'"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
            	'"apply-actions": {"action": [{"output-action": {'\
            	'"output-node-connector": "1"},"order": "0"}]}}]},'\
            	'"priority": "105","cookie": "1","table_id": "0"}]}'

		headers = {'Content-type': 'application/json'}
		#下发流表
		#下发s2、s3和s1的流表
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1', body=s2_2to1, method='PUT',headers=headers)	
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/1', body=s3_2to1, method='PUT',headers=headers)
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1', body=s1_234to1, method='PUT',headers=headers)
		#默认下发h2数据包从s4的1端口出的流表			
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/41', body=h2_to_s4_1, method='PUT',headers=headers)
		#默认下发h3数据包从s4的1端口出的流表		
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/51', body=h3_to_s4_1, method='PUT',headers=headers)
		#默认下发h4数据包从s4的1端口出的流表		
		response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/61', body=h4_to_s4_1, method='PUT',headers=headers)

		while(True):
			#获取s4端口1的流量
			uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:4/node-connector/openflow:4:1'
			response, content = http.request(uri=uri, method='GET')
			content = json.loads(content)
			statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
			bytes1 = statistics['bytes']['transmitted']
			#1秒后再次获取
			time.sleep(1)
			response, content = http.request(uri=uri, method='GET')
			content = json.loads(content)
			statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
			bytes2 = statistics['bytes']['transmitted']
			#在检测到s4的1口流量空闲时发的流表
			speed=float(bytes2-bytes1)/1
			if speed !=0 :
				if speed < 1200 :
					print 's4端口1空闲，数据包从1口通过 ','speed =',speed
				#下发默认的流表			
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/41', body=h2_to_s4_1, method='PUT',headers=headers)	
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/51', body=h3_to_s4_1, method='PUT',headers=headers)	
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/61', body=h4_to_s4_1, method='PUT',headers=headers)
				#在检测到s2的1口流量满载时下发新的流表
				else :
					print 's4端口1满载，为均衡负载，数据从2，3口通过 ','speed =',speed
				#设置h2数据包的流表
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/41', body=lh2_to_s4_1, method='PUT',headers=headers)
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/42', body=h2_to_s4_2, method='PUT',headers=headers)
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/43', body=h2_to_s4_3, method='PUT',headers=headers)
				#设置h3数据包的流表
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/52', body=h3_to_s4_2, method='PUT',headers=headers)
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/53', body=h3_to_s4_3, method='PUT',headers=headers)
				#设置h4数据包的流表
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/62', body=h4_to_s4_2, method='PUT',headers=headers)
					response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/63', body=h4_to_s4_3, method='PUT',headers=headers)


odl = OdlUtil('127.0.0.1', '8181')
odl.install_flow()
