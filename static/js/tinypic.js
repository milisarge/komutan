function showTinypicPlugin(){
    var el = document.getElementById('tinypic_plugin_333');
    el.style.display = '';
    if (el.src != '')
    {
        return;
    }
    var w = 250;
    var h = 480;
    curl = '';
    ctxt = '';
        
    if (typeof(tinypic_layout) == 'undefined') {
        tinypic_layout = 'narrow';
    } else {
        if (tinypic_layout == 'wide') {
            w = 480;
            h = 400;
        }
    }
    if (typeof(tinypic_type) == 'undefined')
        tinypic_type = 'both';
    if (typeof(tinypic_links) == 'undefined')
        tinypic_links = 'html';
    if (typeof(tinypic_language) == 'undefined')
        tinypic_language = 'en';
    if (typeof(tinypic_search) == 'undefined') 
        tinypic_search = 'true';
    if (typeof(tinypic_callback_url) != 'undefined')
        curl = "|cu,"+tinypic_callback_url.replace(/\&/g, '%26');;
    if (typeof(tinypic_callback_text) != 'undefined')
        ctxt = "|ct,"+tinypic_callback_text.replace(/\&/g, '%26');;
    
    el.setAttribute("height", h);
    el.setAttribute("width", w);
    el.setAttribute("scrolling", "no");

    var tpurl = "http://plugin.tinypic.com/plugin/index.php?popts=l,"+tinypic_layout+"|t,"+tinypic_type+"|c,"+tinypic_links+"|i,"+tinypic_language+"|s,"+tinypic_search;
    if (curl)
        tpurl += curl;
    if (ctxt)
        tpurl += ctxt;
    el.src = tpurl;
}

function hideTinypicPlugin(){
    var el = document.getElementById('tinypic_plugin_333');
    el.style.display = 'none';
}

//var id=Math.floor(Math.random()*1000000);
document.write("<iframe id='tinypic_plugin_333' frameborder='0' style='display: none;' scrolling='no'></iframe><br/>");

showTinypicPlugin();
 
    
