$(document).ready(function (e) {

    var showForm = function (e) {
        btn = $(this)
        $.ajax({
            url: btn.data('url'),
            type: "get",
            dataType: "json",
            beforeSend: function (data) {
                $("#exampleModal").modal('show')
            },
            success: function (data) {
                $("#exampleModal .modal-content").html(data.html_form)

            }
        })
    };
    var saveBook = function (e) {
        e.preventDefault()
        form = $(this)
        $.ajax({
            url: form.attr('action'),
            type: "post",
            data: form.serialize(),
            success: function (data) {
                $("tbody").html(data.books)
                $("#exampleModal").modal('hide')
            }
        })
    }

    //CreateForm
    $(document).on('click', '#createBookForm', showForm)
    $("#exampleModal").on('submit', '#createForm', saveBook)
    //UpdateForm
    $(document).on('click', '.EditBtn', showForm)
    $("#exampleModal").on('submit', '#updateForm', saveBook)

    //DeleteForm
    $(document).on('click', '.deleteBtn', showForm)
    $("#exampleModal").on('submit', '#deleteForm', saveBook)


})
