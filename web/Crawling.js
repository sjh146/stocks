
     // Function to send checkbox state to Python
    async function sendCheckboxState() {
        const MP = document.getElementById("MarketPrice");
        const TV = document.getElementById("TradingVolume");
        const CL = document.getElementById("CostLiness");
        const LP = document.getElementById("LowPrice");
        const BP = document.getElementById("BidPrice");

        const MP_V = document.getElementById("MarketPrice").value;
        const TV_V = document.getElementById("TradingVolume").value;
        const CL_V = document.getElementById("CostLiness").value;
        const LP_V = document.getElementById("LowPrice").value;
        const BP_V = document.getElementById("BidPrice").value;

        const MP_Checked = MP.checked;
        const TV_Checked = TV.checked;
        const CL_Checked = CL.checked;
        const LP_Checked = LP.checked;
        const BP_Checked = BP.checked;
        // Call Python function with checkbox state
        const MP_response = await eel.handle_checkbox_state(MP_Checked,MP_V)();
        document.getElementById("MP_O").innerText = MP_response;
        const TV_response = await eel.handle_checkbox_state(TV_Checked,TV_V)();
        document.getElementById("TV_O").innerText = TV_response;
        const CL_response = await eel.handle_checkbox_state(CL_Checked,CL_V)();
        document.getElementById("CL_O").innerText = CL_response;
        const LP_response = await eel.handle_checkbox_state(LP_Checked,LP_V)();
        document.getElementById("LP_O").innerText = LP_response;
        const BP_response = await eel.handle_checkbox_state(BP_Checked,BP_V)();
        document.getElementById("BP_O").innerText = BP_response;
        eel.get_start()
    }
   
