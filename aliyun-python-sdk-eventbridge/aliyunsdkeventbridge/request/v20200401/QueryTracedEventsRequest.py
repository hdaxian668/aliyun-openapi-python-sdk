# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class QueryTracedEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'QueryTracedEvents')
		self.set_method('POST')

	def get_MatchedRule(self): # String
		return self.get_query_params().get('MatchedRule')

	def set_MatchedRule(self, MatchedRule):  # String
		self.add_query_param('MatchedRule', MatchedRule)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_EventBusName(self): # String
		return self.get_query_params().get('EventBusName')

	def set_EventBusName(self, EventBusName):  # String
		self.add_query_param('EventBusName', EventBusName)
	def get_EventSource(self): # String
		return self.get_query_params().get('EventSource')

	def set_EventSource(self, EventSource):  # String
		self.add_query_param('EventSource', EventSource)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_EventType(self): # String
		return self.get_query_params().get('EventType')

	def set_EventType(self, EventType):  # String
		self.add_query_param('EventType', EventType)
