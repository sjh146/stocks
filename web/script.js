
$(function() {
    
    $("#save").click(function() {
        uun = document.getElementById('un').value;
       
        
        uid = document.getElementById('id').value;
        

        upw = document.getElementById('pw').value;
        
       eel.insert_blog(uun,uid,upw)
       
    });
    $("#delete").click(function() {
        sdata = document.getElementById('search').value;
        eel.delete_blog(sdata)   
    }); 
});