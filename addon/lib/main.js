/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

const {Class} = require("api-utils/heritage");
const {data} = require("self");
const {Factory, Unknown} = require("api-utils/xpcom");
const Observer = require("observer-service");
const {PageMod} = require("page-mod");
const Preferences = require("simple-prefs");
const tabs = require("tabs");
const widgets = require("widget");
const {ImageManager} = require("ImageManager");

const {Ci,Cu} = require("chrome");
Cu.import("resource://gre/modules/Services.jsm");

const IMAGE_SERVER_HOST = "https://up-suggest.vcap.mozillalabs.com";
const gImageManager = new ImageManager(IMAGE_SERVER_HOST);

exports.main = function(options, callbacks) {


  widgets.Widget({
    id: "test",
    label: "test",
    contentURL: data.url("icon.png"),
    onClick: function() {
      console.log("clicked");
      tabs.open(
      {
        url: data.url( "im_test.html"),
        onReady: function ( tab ) {
                  let worker = tab.attach({
                     contentScriptFile: [
                        data.url("jquery-1.7.2.js"),
                        data.url("im_test.js"),
                     ],
                  });

                  worker.port.on("get_image", function(cat) {
                    console.log("category " + cat);
                    gImageManager.getImageForCat(cat, function(imageUrl) {
                      worker.port.emit("show_image",imageUrl);
                    });
                  });
            }
      });
    }
  });

}
