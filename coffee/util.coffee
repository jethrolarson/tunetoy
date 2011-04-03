(($, w, d)->
  util = {}
  # As of 1.5.0 the mobile safari reports wrong values on offset()
  # http://dev.jquery.com/ticket/6446
  if /webkit.*mobile/i.test(navigator.userAgent)
    $.fn.offsetOld = $.fn.offset
    $.fn.offset = ->
      result = @offsetOld()
      result.top -= w.scrollY
      result.left -= w.scrollX
      return result
)(jQuery,window,document)