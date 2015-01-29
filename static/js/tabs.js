/**
 * Created by piratos on 12/30/14.
 */

   $("#to_type").click(function(){
       $("#status").removeClass("active").addClass("fade");
       $("#type1").removeClass("fade").addClass("active");
       $("gov1").removeClass("active").addClass("fade");
       console.log("tabs");
   });
   $("#to_gov").click(function(){
       $("#status").removeClass("active").addClass("fade");
       $("#type1").removeClass("active").addClass("fade");
       $("#gov1").removeClass("fade").addClass("active");
       console.log("tabs");
   });