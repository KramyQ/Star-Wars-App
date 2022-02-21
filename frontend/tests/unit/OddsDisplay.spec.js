import { shallowMount, mount } from "@vue/test-utils";

import oddsDisplay from "@/components/oddsPrediction/oddsDisplay";

describe("oddsDisplay.vue", () => {
  it("oddsDisplay showsno result",  () => {
    const wrapper = shallowMount(oddsDisplay, {props: {
        successRate: {
          value: 0,
          status: false
        }}})
    expect(wrapper.find('#successValue').exists()).toBe(false)
  })
  it("oddsDisplay shows result",  () => {
    const wrapper = shallowMount(oddsDisplay, {props: {
        successRate: {
          value: 0,
          status: true
        }}})
    expect(wrapper.find('#successValue').exists()).toBe(true)
  })
})
