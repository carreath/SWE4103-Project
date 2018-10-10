<template>
  <div id="weather-widget">
    <a
      class="weatherwidget-io"
      href="https://forecast7.com/en/45d96n66d64/fredericton/"
      :data-mode="weatherMode"
      :data-days='daysToShow'
      data-theme="pure"
      data-basecolor="#fcfcfc"
      data-textcolor="#003a99"
      data-mooncolor="#003a99"
      data-cloudcolor="#003a99"
      data-cloudfill="#fcfcfc"
      data-snowcolor="#003a99">
    </a>
  </div>
</template>

<script>
/* eslint-disable */
export default{
  name: 'WeatherWidget',
  data() {
    return {
      weatherMode: 'Forecast',
      daysToShow: 3,
    };
  },
  mounted() {
    let width = window.innerWidth
      || document.documentElement.clientWidth
      || document.body.clientWidth;
    if (width < 560) {
      return;
    }
    if (width < 780) {
      this.weatherMode = 'Current';
    }

    !function(d,s,id){
      var js,fjs=d.getElementsByTagName(s)[0];
      if(!d.getElementById(id)){
        js=d.createElement(s);
        js.id=id;
        js.src='https://weatherwidget.io/js/widget.min.js';
        fjs.parentNode.insertBefore(js,fjs);
      }
    }(document,'script','weatherwidget-io-js');
  },
};
</script>

<style lang='scss'>
#weather-widget{
  max-height: 100%;

  a{
    border-radius: 16px;
    max-height: 98px;
  }
}
</style>
