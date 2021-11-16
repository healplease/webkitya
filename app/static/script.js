$( document ).ready(function () {
    var labelInitialText = $("input.upload-files-button").closest(".form-group").find("label").text();

    $("button.close").click(function () {
        $(this).closest(".alert").fadeOut("fast");
    });

    $("input.upload-files-button").change(function () {
        var label = $(this).closest(".form-group").find("label");
        var filesUploaded = $(this)[0].files.length;
        label.text(labelInitialText + ` (${filesUploaded} files uploaded)`)
    });
});
