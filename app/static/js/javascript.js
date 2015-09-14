$(document).ready(function(){
	$(".pp").click(function(){
	var form_data = new FormData($('#formid')[0])
	alert(form_data)
          $.ajax({
              type: 'POST',
              url: '/about',
              data:form_data,
              contentType: false,
              processData: false,
              success: function(response) {
                document.write(response)
              },

              error: function() {
                alert('error in finding result')
              }
          })
    })
})