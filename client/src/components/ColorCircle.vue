<template>
  <div
    id="circle"
    :style="{ 'background-color': teamColorHex, }">
  </div>
</template>

<script>
export default {
  name: 'ColorCircleTeamName',
  props: {
    teamColorHex: String,
  },
};
</script>

<style scoped lang="scss">
#circle {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 8px;
}
</style>
