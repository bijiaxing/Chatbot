'''思路记录：
整个程序启示检索由两大类 三个列表组成：
分辨是： 
  一、起始类  list1=[单轮检索问题] list2=[多轮检索起始问题]  这两大列表永远不变
  二、进行中类 list3=[多轮检索中间问题]  该列表一直变化

流程如下：
先检测是不是多轮对话的中间问题 ：如果是、则继续多轮对话不考虑单轮对话，并且根据多轮对话的进程（state）更新list3，如果不是，则注销“会话实例”，离开“进行类”，通用也要注销list3
再检测是不是多轮对话的起始问题： 如果是，则创建对应的会话实例、创建list3
最后检测是不是单轮检索问题
总之、不论是何种会话方式、list3都是要变化的

content="开始"
multi_round_start=['开始']
multi_round_process=[]
if len(multi_round_process): #如果非空的话
    if content in multi_round_process:
        response=dialoge.changestate(content) #
        updata(multi_round_process) #更新多轮对话表
        return response 
    else:
        cancel(dialoge) #注销掉对话对象
        multi_round_process=[] #多轮对话表滞空
if content in multi_round_start:
    dialoge=new agent()
    response=dialoge.changestate(content)
    updata(multi_round_process) #更新多轮对话表
    return response
if content in jiansuo:
'''