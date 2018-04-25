$(document).ready(function (e) {


    $("#createBookForm").on('click',function (e) {
        $.ajax({
            url:"/createBook/",
            type:"get",
            dataType:"json",
            beforeSend:function (data) {
                $("#exampleModal").modal('show')
            },
            success:function (data) {
                $("#exampleModal .modal-content").html(data.html_form)

            }
        })
    })

    $("#exampleModal").on('submit','#saveForm',function (e) {
        e.preventDefault()
        form=$(this)

        $.ajax({
            url: "/createBook/",
            type:"post",
            data: form.serialize(),
            success: function (data) {
                 console.log(data)
                $("#id_title").val("")
            }
        })

    })


})
