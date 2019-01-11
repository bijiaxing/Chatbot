 window.onload = function()
 {
            var arrIcon = ['http://www.xttblog.com/icons/favicon.ico','http://www.xttblog.com/wp-content/uploads/2016/03/123.png'];
            var num = 1;     //控制头像改变
            var iNow = -1;    //用来累加改变左右浮动
            var icon = document.getElementById('user_face_icon').getElementsByTagName('img');
            var btn = document.getElementById('btn');
            var text = document.getElementById('text');
            var content = document.getElementsByTagName('ul')[0];
            var img = content.getElementsByTagName('img');
            var span = content.getElementsByTagName('span');
            icon[0].onclick = function(){
                if(num==0){
                    this.src = arrIcon[1];
                    num = 1;
                }else if(num==1){
                    this.src = arrIcon[0];
                    num = 0;
                }                
            }
            btn.onclick = function()
            {
                if(text.value =='')
                {
                    alert('不能发送空消息');
                }else 
                {
                   num = -num;       
                   content.innerHTML += '<li><img src="'+arrIcon[1]+'" class = "imgright"><span class = "spanright">'+text.value+'</span></li>';
                    $.get( "http://127.0.0.1:5000/chatbot?content="+text.value, function( data )
                     {
                        content.innerHTML += '<li><img src="'+arrIcon[0]+'" class = "imgleft"><span class = "spanleft">'+data.as+'</span></li>';
                     }, "json");
                    text.value = '';
                    // 内容过多时,将滚动条放置到最底端
                    content.scrollTop=content.scrollHeight;  
                }
             }
        }