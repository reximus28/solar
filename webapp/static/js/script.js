document.addEventListener('DOMContentLoaded', function () {
    const panelsOrderedField = document.getElementById('id_panels_ordered');
    const invertersOrderedField = document.getElementById('id_inverters_ordered');
    const totalCostSpan = document.getElementById('total-cost');

    function updateTotalCost() {
        const panelsCost = parseFloat(Array.from(panelsOrderedField.selectedOptions).reduce((acc, option) => acc + parseFloat(option.getAttribute('data-price')), 0) || 0);
        const invertersCost = parseFloat(Array.from(invertersOrderedField.selectedOptions).reduce((acc, option) => acc + parseFloat(option.getAttribute('data-price')), 0) || 0);

        const totalCost = (panelsCost + invertersCost).toFixed(2);
        totalCostSpan.textContent = totalCost;
    }

    panelsOrderedField.addEventListener('change', updateTotalCost);
    invertersOrderedField.addEventListener('change', updateTotalCost);

    // Initial update
    updateTotalCost();
});