(()=>{"use strict";var e,t={1293:(e,t,o)=>{var r=o(5311),a=o.n(r),i=o(6024);class n extends i.D_{ajaxifyLinks(e,t){super.ajaxifyLinks(e,t),a()("a.upload-one-now").on("click",(e=>{const t=a()("#id_collection_id").val();t&&a()("#id_image-chooser-upload-collection").val(t),e.preventDefault()}))}onLoadChooseStep(e){super.onLoadChooseStep(e),a()("a.suggested-tag").on("click",(e=>(a()("#id_q").val(""),this.searchController.search({tag:a()(e.currentTarget).text(),collection_id:a()("#id_collection_id").val()}),!1)))}onLoadDuplicateFoundStep(e,t){a()("#tab-upload",e.body).replaceWith(t.htmlFragment),a()(".use-new-image",e.body).on("click",(t=>(e.loadUrl(t.currentTarget.href),!1))),a()(".use-existing-image",e.body).on("click",(t=>{var o=a()(t.currentTarget).closest("form"),r=a()('input[name="csrfmiddlewaretoken"]',o).val();return e.postForm(t.currentTarget.href,{csrfmiddlewaretoken:r}),!1}))}onLoadSelectFormatStep(e){var t=document.querySelector("#id_image-chooser-insertion-image_is_decorative"),o=document.querySelector("#id_image-chooser-insertion-alt_text"),r=document.querySelector('[for="id_image-chooser-insertion-alt_text"]');function i(){o.setAttribute("disabled","disabled"),r.classList.remove("required")}function n(){o.removeAttribute("disabled"),r.classList.add("required")}t.checked?i():n(),t.addEventListener("change",(e=>{e.target.checked?i():n()})),a()("form",e.body).on("submit",(t=>(a().post(t.currentTarget.action,a()(t.currentTarget).serialize(),e.loadResponseText,"text"),!1)))}getOnLoadHandlers(){const e=super.getOnLoadHandlers();return e.duplicate_found=(e,t)=>{this.onLoadDuplicateFoundStep(e,t)},e.select_format=(e,t)=>{this.onLoadSelectFormatStep(e,t)},e}}window.IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS=new n({creationFormFileFieldSelector:"#id_image-chooser-upload-file",creationFormTitleFieldSelector:"#id_image-chooser-upload-title",creationFormEventName:"wagtail:images-upload",creationFormTabSelector:"#tab-upload"}).getOnLoadHandlers();class l extends i.sf{constructor(){super(...arguments),this.onloadHandlers=window.IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS}}window.ImageChooserModal=l},5311:e=>{e.exports=jQuery}},o={};function r(e){var a=o[e];if(void 0!==a)return a.exports;var i=o[e]={exports:{}};return t[e](i,i.exports,r),i.exports}r.m=t,e=[],r.O=(t,o,a,i)=>{if(!o){var n=1/0;for(s=0;s<e.length;s++){for(var[o,a,i]=e[s],l=!0,d=0;d<o.length;d++)(!1&i||n>=i)&&Object.keys(r.O).every((e=>r.O[e](o[d])))?o.splice(d--,1):(l=!1,i<n&&(n=i));if(l){e.splice(s--,1);var c=a();void 0!==c&&(t=c)}}return t}i=i||0;for(var s=e.length;s>0&&e[s-1][2]>i;s--)e[s]=e[s-1];e[s]=[o,a,i]},r.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return r.d(t,{a:t}),t},r.d=(e,t)=>{for(var o in t)r.o(t,o)&&!r.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),r.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.j=813,(()=>{var e={813:0};r.O.j=t=>0===e[t];var t=(t,o)=>{var a,i,[n,l,d]=o,c=0;if(n.some((t=>0!==e[t]))){for(a in l)r.o(l,a)&&(r.m[a]=l[a]);if(d)var s=d(r)}for(t&&t(o);c<n.length;c++)i=n[c],r.o(e,i)&&e[i]&&e[i][0](),e[i]=0;return r.O(s)},o=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))})();var a=r.O(void 0,[751],(()=>r(1293)));a=r.O(a)})();