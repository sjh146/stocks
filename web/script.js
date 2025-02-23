
$(function() {
    
    $("#save").click(function(usn,uid,upw) {
        usn = document.getElementById('sn').value;
        document.getElementById("result1").innerText = usn;
        
        uid = document.getElementById('id').value;
        document.getElementById("result2").innerText = uid; 

        upw = document.getElementById('pw').value;
        document.getElementById("result3").innerText = upw; 
       
        eel.get_blog_list(usn,uid,upw)
    });
    $("#btn").click(function(uid,upw) {
        eel.crawl(uid,upw)
    });
    $("#sbtn").click(function() {
        
    });
});