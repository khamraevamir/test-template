$(function(){
    $('.addToCart').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = $(this).attr('data-url')
        let id = $(this).attr('data-id')
        let quantity = $(this).parent().find('input').val()

        if(quantity == ''){
            alert('Plese field the blank')
        } else{
            $.ajax({
                url:url,
                type:'POST',
                data:{id, quantity},
                headers:{
                    'X-CSRFToken':token
                },
                
    
                success: (data)=>{
                    $('.cart_quant').load( ' .cart_quant_val ')
                    alert(data)
                    console.log(data)
    
                    btn.parent().find('input').val('')
                },
    
                error: (msg)=> {
                    console.log(msg)
                }
            })   
        }
        
    })
})