// alert('hi');
var jQuery;


var up_to_class = function(elt, cls)
{
    var candidate = elt;
    while(elt){
        if (jQuery(elt).hasClass(cls))
        {
            return elt;
        }
        // document.parentNode == null.
        elt = elt.parentNode;
    }
    return null;
};


var star_handler = function(event){
    //    alert(event.data);
    var talk = up_to_class(event.target, 'talk');
    jQuery(talk).removeClass('score-0 score-1 score-2 score-3');
    jQuery(talk).addClass('score-' + event.data);
    //    alert(talk);
};


var by_score_handler = function(event){

    var by_score = up_to_class(event.target, 'by-score');
    jQuery('.talk').hide();
    jQuery('.talk.score-' + event.data).show();
    // Needed if current active talk is hidden.
    jQuery('#talks').accordion('option', 'active', false);
};


var by_score_all_handler = function(event){

    var by_score = up_to_class(event.target, 'by-score');
    jQuery('.talk').show();
    jQuery('#talks').accordion('option', 'active', false);
};


var ready_handler = function()
{
    var i;
    for(i = 0; i <= 3; i++)
    {
        jQuery('.star-' + i).on('click', i, star_handler);
        jQuery('.by-score-' + i).on('click', i, by_score_handler);
    }

    jQuery('.by-score-all').on('click', by_score_all_handler);
    jQuery('#talks').accordion({
        active: false,
        collapsible: true,
        header: '.talk'
    });
};



jQuery(document).ready(ready_handler);
