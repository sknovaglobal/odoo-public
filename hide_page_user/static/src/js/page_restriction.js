/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { FormController } from '@web/views/form/form_controller';
import { jsonrpc } from '@web/core/network/rpc_service';
import { onMounted, onPatched } from '@odoo/owl';

patch(FormController.prototype, {
    setup() {
        super.setup();

        this.pageConfigurations = [];

        // Fetch config once
        this._loadConfig();

        // Run after first render
        onMounted(() => {
            this._applyHide();
        });

        // Run after every re-render (IMPORTANT)
        onPatched(() => {
            this._applyHide();
        });
    },

    async _loadConfig() {
        try {
            const result = await jsonrpc('/get_user_page_configurations', {});
            this.pageConfigurations = result || [];
            console.log('Fetch result:', result);
        } catch (error) {
            console.error('Error fetching user page configurations:', error);
        }
    },

    _applyHide() {
        if (!this.pageConfigurations.length) return;

        this.pageConfigurations.forEach((pageName) => {
            const el = document.querySelector(`[name="${pageName}"]`);
            if (el) {
                el.style.display = 'none';
                console.log(`Hiding page: ${pageName}`);
            }
        });
    },
});