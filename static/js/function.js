$(function () {
  document
    .querySelectorAll('a')
    .forEach(e => e.classList.remove('active', 'w3-blue-grey'))
})
let changeSidebar = function (nav_treeview) {
    let father = document.querySelector(nav_treeview)
      // son = document.querySelector(nav_item)
    father.classList.add('active')
    // father.parentElement.classList.add('menu-open')
    // son.classList.add('bg-primary')
    // son.parentElement.parentElement.style.display = 'block'
  },
  message_error = function (obj) {
    let html = ``
    if (typeof obj === 'object') {
      html = `<ul style="text-align: left;">`
      $.each(obj, function (key, value) {
        html += `<li>${key}: ${value}</li>`
      })
      html += `</ul>`
    } else html = `<p>${obj}</p>`
    Swal.fire({
      title: `Error`,
      html: html,
      icon: `error`
    })
  },
  //For Delete using jQuery confirm plugin and Jquery with ajax
  submit_with_ajax_alert = function (url, title, content, parameters, callback, icon) {
    $.confirm({
      theme: 'material',
      title: title,
      icon: icon,
      content: content,
      columnClass: 'small',
      typeAnimated: true,
      cancelButtonClass: 'bg-gradient-primary circular',
      draggable: true,
      dragWindowBorder: false,
      buttons: {
        info: {
          text: 'Yes',
          btnClass: 'bg-gradient-primary circular',
          action: function () {
            ajaxFunction(url, parameters, callback)
          }
        },
        danger: {
          text: 'No',
          btnClass: 'bg-gradient-danger circular',
          action: () => {
          }
        }
      }
    })
  },
  //For add | update using jQuery with ajax
  submit_with_ajax = (url, parameters, callback) =>
    ajaxFunction(url, parameters, callback),
  //Auxiliary method: submit with ajax and jQuery
  ajaxFunction = function (url, parameters, callback, async = true) {
    $.ajax({
      url: url,
      type: 'POST',
      data: parameters,
      dataType: 'json',
      processData: false,
      contentType: false,
      async: async
    })
      .done(function (data) {
        console.log(data)
        if (!data.hasOwnProperty('error')) {
          callback(data)
          return false
        }
        if (data['error'].toString().includes('UNIQUE'))
          message_error(`There is already a ${ent} with this name`)
        else message_error(data.error)
      })
      .fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown)
      })
      .always(function (data) {
      })
  },
  testFetch = () => console.log('fetch'),
  //Jquery confirm alert
  alert_action = function (title, content, callback, cancel, icon) {
    $.confirm({
      theme: 'material',
      title: title,
      icon: icon,
      content: content,
      columnClass: 'small',
      typeAnimated: true,
      cancelButtonClass: 'bg-gradient-primary circular',
      draggable: true,
      dragWindowBorder: false,
      buttons: {
        info: {
          text: 'Yes',
          btnClass: 'bg-gradient-primary circular',
          action: () => callback()
        },
        danger: {
          text: 'No',
          btnClass: 'bg-gradient-red circular',
          action: () => cancel()
        }
      }
    })
  },
  Toast = (text, icon = 'success') => {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 5000
    })
    Toast.fire({
      icon: icon,
      title: text
    })
  },
  truncate = (str, len, end = '..') =>
    str.replace(new RegExp('(.{' + len + '}).*'), '$1' + end + '')
