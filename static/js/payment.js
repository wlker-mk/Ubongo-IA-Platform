// Payment method selection
        document.querySelectorAll('input[name="payment-method"]').forEach(radio => {
            radio.addEventListener('change', function() {
                // Remove active class from all options
                document.querySelectorAll('.payment-option').forEach(option => {
                    option.classList.remove('active');
                });

                // Add active class to selected option
                this.closest('.payment-option').classList.add('active');

                // Show/hide card form
                const cardForm = document.getElementById('card-form');
                if (this.value === 'stripe') {
                    cardForm.style.display = 'block';
                } else {
                    cardForm.style.display = 'none';
                }
            });
        });

        // Format card number input
        document.getElementById('card-number').addEventListener('input', function(e) {
            let value = e.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
            let formattedValue = value.match(/.{1,4}/g)?.join(' ') || value;

            if (formattedValue.length <= 19) {
                this.value = formattedValue;
            }
        });

        // Format expiry date input
        document.getElementById('expiry').addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 2) {
                value = value.substring(0,2) + '/' + value.substring(2,4);
            }
            this.value = value;
        });

        // Format CVC input
        document.getElementById('cvc').addEventListener('input', function(e) {
            this.value = this.value.replace(/\D/g, '');
        });

        // Form submission
        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Paiement simulé - Fonctionnalité de démonstration');
        });

        // Cancel payment
        document.querySelector('.btn-secondary').addEventListener('click', function() {
            if (confirm('Êtes-vous sûr de vouloir annuler le paiement ?')) {
                window.history.back();
            }
        });