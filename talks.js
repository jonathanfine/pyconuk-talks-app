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


var ready_handler = function()
{
    var i;
    for(i = 0; i <= 3; i++)
    {
        jQuery('.star-' + i).on('click', i, star_handler);
    }

};



jQuery(document).ready(ready_handler);
