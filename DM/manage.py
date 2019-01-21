from DiaTree import *
root=""
with open("Multi_dia.json",'r',encoding='UTF-8') as load_f:
    load_dict = json.load(load_f)
    root=ChangeDictToTree(load_dict)
content="开始"
multi_round_start=[]  #多轮对话开始列表
multi_round_start.append(root)
multi_round_process=[]   #多轮对话中间列表

def check(content,multi_round_start,multi_round_process):
######################如果中间列表非空的话######################
    if len(multi_round_process): 
        for member in multi_round_process:
            if content==member.question:
                response=member.response 
                multi_round_process[:]=member.child_list #更新给用户选择的列表
                return response 
           
######################中间列表空###############################        
    for member in multi_round_start:
        if content==member.question: #如果用户问题出现在开始列表当中 
            response=member.response
            multi_round_process[:]=member.child_list#更新给用户选择的列表
            return response
            
######################中间列表只要没有更新则滞空###############################  
    del multi_round_process[:]
 
content=input('请输入')
while content is not '0':
    print(check(content,multi_round_start,multi_round_process))
    content=input('请')



