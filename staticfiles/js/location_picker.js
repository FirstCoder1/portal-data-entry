!function(e){function t(){var t=e(d);if(0!==t.length){c=e(u),l=e(s);var o=c.val()&&l.val();o&&(f=parseFloat(c.val()),g=parseFloat(l.val()),m=v),t.after(e('<div class="js-setloc-map setloc-map"></div>'));var p=document.getElementsByClassName("js-setloc-map")[0];i=new google.maps.Map(p,{zoom:m,center:{lat:f,lng:g}}),r=new google.maps.Marker({map:i,draggable:!0}),o&&n(f,g),google.maps.event.addListener(i,"click",function(e){n(e.latLng.lat(),e.latLng.lng())}),google.maps.event.addListener(r,"dragend",function(){a(r.getPosition().lat(),r.getPosition().lng())})}}function n(e,t){r.setPosition({lat:e,lng:t}),a(e,t)}function a(e,t){o(c,e),o(l,t)}function o(e,t){var n=e.prop("step"),a=0;n&&(2==n.split(".").length&&(a=n.split(".")[1].length),t=t.toFixed(a)),e.val(t)}var i,r,c,l,d=".form-row.field-longitude",u="#id_latitude",s="#id_longitude",f=51.516448,g=-.130463,m=6,v=12;e(document).ready(function(){t()})}(django.jQuery);