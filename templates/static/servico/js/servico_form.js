document.addEventListener("DOMContentLoaded", function () {
    const servicoCheckboxes = document.querySelectorAll('input[name="servico"]');
    const valorTotalInput = document.querySelector('input[name="valor_total"]');

    servicoCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            
            let totalCalculado = 0;
            servicoCheckboxes.forEach(checkbox => {
                if (checkbox.checked) {
                    const preco = parseFloat(checkbox.getAttribute('data-preco'));
                    if (!isNaN(preco)) {
                        totalCalculado += preco;
                    }
                }
                console.log(totalCalculado);
            }); 

            valorTotalInput.value = totalCalculado.toFixed(2);
        });
    });
});
