document.addEventListener('DOMContentLoaded', (event) => {
    let company_info = document.getElementById('company_info');

    document.getElementById('if_executive').onclick = function() {
        if (this.checked)
            {
                company_info.style.display = "none";
            } else {
                company_info.style.display = "block";
            }
    }
});
