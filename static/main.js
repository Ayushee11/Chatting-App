console.log('Hello')

var socket=io.connect(location.protocol+'//'+document.domain+':'+location.port)

function send()
{
	var msgBox=document.getElementsById('msgBox')
	socket.emit('msg',msgBox.value)
	msgBox.value=""
}

socket.on('push',function(data){
	var msgList.innerHTML+="<p>"+data+"</p>"
})











function fetchUsers(){
	fetch('/users').then(function(res) {
		res.json().then(function(data){
			console.log(data)
		})
		// body...
	})
}
 var socket = io();
  //  socket.on('connect', function() {
    //    socket.emit('my event', {data: 'I\'m connected!'});
    //});