document.addEventListener('DOMContentLoaded', (event) => {
    let company_name = document.getElementById('div_id_company_name');
    let company_nip = document.getElementById('div_id_nip');

    document.getElementById('if_executive').onclick = function() {
        if (this.checked)
            {
                company_name.style.display = "none";
                company_nip.style.display = "none";
            } else {
                company_name.style.display = "block";
                company_nip.style.display = "block";
            }
    }
});
