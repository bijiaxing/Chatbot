class RequestBasicsAgent(Agent):
    """ A simple agent to test the system. This agent should simply request all the basic slots and then issue: thanks(). """
    def initialize_episode(self):
        self.state = {}  "state 是词典，记录了行为diaact、轮数turn、通知槽、问题槽等等信息"
        self.state['diaact'] = 'UNK'  "表行为"
        self.state['inform_slots'] = {}
        self.state['request_slots'] = {}
        self.state['turn'] = -1
        self.current_slot_id = 0
        self.request_set = ['moviename', 'starttime', 'city', 'date', 'theater', 'numberofpeople']
        self.phase = 0

    def state_to_action(self, state):
        """ Run current policy on state and produce an action """
        
        self.state['turn'] += 2
        if self.current_slot_id < len(self.request_set):
            slot = self.request_set[self.current_slot_id]       "slot表示当前要询问的内容"
            self.current_slot_id += 1                           "下次要询问的内容+1"

            act_slot_response = {}         "表回答，也是一个词典,由回答的行为、轮数、通知槽、请求槽"
            act_slot_response['diaact'] = "request"  
            act_slot_response['inform_slots'] = {}
            act_slot_response['request_slots'] = {slot: "UNK"}
            act_slot_response['turn'] = self.state['turn']
        elif self.phase == 0:     "表回答完毕，已经得到了想要的信息，想让人确定一下"
            act_slot_response = {'diaact': "inform", 'inform_slots': {'taskcomplete': "PLACEHOLDER"}, 'request_slots': {}, 'turn':self.state['turn']}
            self.phase += 1 
        elif self.phase == 1:         "表结束语，谢谢"
            act_slot_response = {'diaact': "thanks", 'inform_slots': {}, 'request_slots': {}, 'turn': self.state['turn']}
        else:
            raise Exception("THIS SHOULD NOT BE POSSIBLE (AGENT CALLED IN UNANTICIPATED WAY)")
        return {'act_slot_response': act_slot_response, 'act_slot_value_response': None}



class TreeAgent(Agent):
    """ A simple agent to test the system. This agent should simply request all the basic slots and then issue: thanks(). """
    def initialize_episode(self):
        self.state = {}  "state 是词典，记录了行为diaact、轮数turn、通知槽、问题槽等等信息"
        self.state['diaact'] = 'UNK'  "表行为"
        self.state['inform_slots'] = {}
        self.state['request_slots'] = {}
        self.state['turn'] = -1
        self.current_slot_id = 0
        self.request_set = ['moviename', 'starttime', 'city', 'date', 'theater', 'numberofpeople']
        self.phase = 0

    def state_to_action(self, state):
        """ Run current policy on state and produce an action """
        
        self.state['turn'] += 2
        if self.current_slot_id < len(self.request_set):
            slot = self.request_set[self.current_slot_id]       "slot表示当前要询问的内容"
            self.current_slot_id += 1                           "下次要询问的内容+1"

            act_slot_response = {}         "表回答，也是一个词典,由回答的行为、轮数、通知槽、请求槽"
            act_slot_response['diaact'] = "request"  
            act_slot_response['inform_slots'] = {}
            act_slot_response['request_slots'] = {slot: "UNK"}
            act_slot_response['turn'] = self.state['turn']
        elif self.phase == 0:     "表回答完毕，已经得到了想要的信息，想让人确定一下"
            act_slot_response = {'diaact': "inform", 'inform_slots': {'taskcomplete': "PLACEHOLDER"}, 'request_slots': {}, 'turn':self.state['turn']}
            self.phase += 1 
        elif self.phase == 1:         "表结束语，谢谢"
            act_slot_response = {'diaact': "thanks", 'inform_slots': {}, 'request_slots': {}, 'turn': self.state['turn']}
        else:
            raise Exception("THIS SHOULD NOT BE POSSIBLE (AGENT CALLED IN UNANTICIPATED WAY)")
        return {'act_slot_response': act_slot_response, 'act_slot_value_response': None}
        

