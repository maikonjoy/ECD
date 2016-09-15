 $(document).ready(function () {
        $('#incluir').on('click', function () {
            //populate the textbox		
            $('#formServico').each(function () {
                this.reset();
            });
            $('#formServico').attr("action", "i_servico");
            $("#myModal").modal();
           
        });

       
        $('#id_IdentificadorCategoria').on('change', function () {
            var categoriaID = $(this).val();
            alert(categoriaID);
            jQuery.ajax({
                async: false,
                type: "POST",
                url: "subCategorias",
                data: "idCategoria: 10",  csrfmiddlewaretoken{% csrf_token %}}, //+ $('#id_IdentificadorCategoria').val(),
                success: function (response) {
                    result = JSON.parse(response);
                    if (result) {
                        // I usually receive a list of items here
                        // I use this list to replace the dependant select                                                

                        $('#id_IdentificadorSubCategoria').empty()  // Use to empty the select

                        // Now we append the industry options we've received
                        for (var i = 0; i < result.item_list.length; i++) {
                            $('#id_IdentificadorSubCategoria').append($('<option>', {
                                value: result.item_list[i]['IdentificadorSubCategoria'],
                                text: result.item_list[i]['DescricaoSubCategoria']
                            }));
                        }

                    } else {
                        console.log('error');
                    }
                }
            })
       

        $('#editar').on('click', function (e) {
            e.preventDefault();
            
		//pega o atributo data-id do botao clicado.
		var itemId = $(this).data('item');
		$("#myModal").modal();
		$('#formServico').attr("action", "a_servico");
	
		var objJSON = jQuery.parseJSON('{ '+ itemId +' }');
		alert(itemId);
		//populate the textbox		
		$("select[name='IdentificadorCategoria']").val(objJSON.IdentificadorCategoria);
		$("select[name='IdentificadorSubCategoria']").val(objJSON.IdentificadorSubCategoria);
		$("input[name='IndicadorTipoServico']").val(objJSON.IndicadorTipoServico);
		$("input[name='ValorHora']").val(objJSON.ValorHora);
		$("textarea[name='DescricaoServico']").val(objJSON.DescricaoServico);
    });
	
 });
