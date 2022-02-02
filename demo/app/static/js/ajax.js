$(function(){
    $('.').on('click', function() {
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = $(this).attr('data-url')

        $.ajax({
            url:url,
            type:'POST',
            headers:{
                'X-CSRFToken':token
            },
            success: (data)=>{
                $('.parent').load( ' .child ')
               
            },

            error: (msg)=> {
                console.log(msg)
            }
        })   
    })
})