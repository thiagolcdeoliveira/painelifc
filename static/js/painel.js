function turma_pesquisar() {
    var select_turma = $("select[name='turma']").val();
    var select_autor = $("select#id_autor_select");
    if (select_turma != "select") {
        $.ajax({
            type: 'GET',
            url: '/cadastro-trabalho/',
            data: {
                turma_id: select_turma,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                // console.log(data);
                var alunos = "<option value='select'>Selecione um autor</option>";
                for (var i = 0; i < data.length; i++) {
                    alunos += '<option value="' + data[i]['id'] + '">' + data[i]['nome'] + '</option>';
                }
                select_autor.html(alunos);
                select_autor.prop('disabled', false);
                $("#id_autor_field > .selection.ui.dropdown.disabled").removeClass("disabled");
                $("#id_autor_field > .selection.ui.dropdown > .text").html("Seleicone um autor");
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    } else {
        select_autor.html("<option value='select'>Seleicone uma turma primeiro</option>");
        $("#id_autor_field > .selection.ui.dropdown > .text").html("Seleicone uma turma primeiro");
        select_autor.prop('disabled', true);
        $("#id_autor_field > .selection.ui.dropdown").addClass("disabled");
    }
}

function adicionar_autor() {
    var select_lista_autores = $("select#id_autor");
    var select_autor = $("select#id_autor_select");
    // console.log();
    if (select_autor != "select") {
        var id = select_autor.val();
        var autor = select_autor.find("[value='" + select_autor.val() + "']").text();
        // select_lista_autores.multiselect({
        //     header: false,
        //     noneSelectedText: "Select"
        // });
        select_lista_autores.append('<option value="' + id + '">' + autor + '</option>');
        // select_lista_autores.multiselect('refresh');
    }
}