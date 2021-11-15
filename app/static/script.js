$( document ).ready(function () {
    $("button.close").click(function () {
        $(this).closest(".alert").fadeOut("fast");
    });
});
