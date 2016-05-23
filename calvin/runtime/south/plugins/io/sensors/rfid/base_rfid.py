# -*- coding: utf-8 -*-

# Copyright (c) 2016 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class RFIDHandlerBase(object):
    def __init__(self, node, rfid_callback):
        super(RFIDHandlerBase, self).__init__()
        
    def request_idl(self):
        pass
        
    def anti_collision(self):
        pass
        
    def select_tag(self, uid):
        pass
        
    def authenticate_classic(self, uid):
        pass
        
    def read_value(self, active_type):
        pass
        
    def write_value(self, active_type, value):
        pass
        
    def initialize(self):
        pass