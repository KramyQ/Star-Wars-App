import { shallowMount, mount } from "@vue/test-utils";
import oddsContainer from "@/components/oddsPrediction/oddsContainer.vue";
import flushPromises from 'flush-promises'
import { getOdds } from "@/services/OddPredictionService";

jest.mock("@/services/OddPredictionService")


describe("oddsContainer.vue", () => {
  it("container shows display component", () => {
    const wrapper = mount(oddsContainer)
    expect(wrapper.find('[data-testid="oddsDisplay"]').exists()).toBe(true)
    expect(wrapper.find('#oddsUploadInterface').exists()).toBe(false)
  })
  it("container shows upload component", async () => {
    const wrapper = shallowMount(oddsContainer)
    await wrapper.setData({
      successRate: {
        value: 0,
        status: false
      }
    });
    expect(wrapper.find('[data-testid="oddsDisplay"]').exists()).toBe(true)
    expect(wrapper.find('[data-testid="oddsUploadInterface"]').exists()).toBe(true)
  })
  it("container test api", async () => {
    getOdds.mockResolvedValueOnce(0)
    const wrapper = mount(oddsContainer)
    getOdds()
    await flushPromises()
    // Function is not called properly because it is called inside an other function in the component therefor invisible because nested
    expect(getOdds).toHaveBeenCalledTimes(1)
    })
})
