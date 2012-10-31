/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
  * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

const file = require("file");
const widgets = require("widget");
const tabs = require("tabs");
const timers = require("timers");
const windows = require("windows");
const simpleStorage = require("simple-storage");
const preferences = require("preferences-service");
const {PageMod} = require("page-mod");
const {data} = require("self");
const request = require("request");

const {Cc,Ci,Cm,Cr,Cu,components} = require("chrome");

Cm.QueryInterface(Ci.nsIComponentRegistrar);

Cu.import("resource://gre/modules/PlacesUtils.jsm", this);
Cu.import("resource://gre/modules/XPCOMUtils.jsm", this);
Cu.import("resource://gre/modules/Services.jsm", this);


function ImageManager(host) {
    this.host = host;
}

ImageManager.prototype = {

   getImageForCat: function(cat,cb) {
     let req = request.Request({
       url: this.host + "/suggest/v1/interest" ,
       headers: { "Interest": cat },
       onComplete: function(response) {
         console.log( "response status" , response.status );
         if( response.status == 200 ){
           console.log(cat + " " + response.json.d);
           if(cb != null){
             cb(response.json.d);
           }
         }
       }
     });

     req.get();
   }
}

exports.ImageManager = ImageManager;


