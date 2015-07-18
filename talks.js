// alert('hi');
var jQuery;

var star_handler = function(event){

    //    alert(event.data);
    var star = event.target;
    var tmp = star;
    var talk = undefined;
    while(!talk) {
        if (jQuery(tmp).hasClass('talk'))
        {
            talk = tmp;
            break;
        }
        // Break if we get to the body element.
        tmp = tmp.parentNode;
    }

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
