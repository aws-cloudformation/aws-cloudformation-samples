package com.awssamples.ec2instancetypes.hook;

import java.util.ArrayList;
import java.util.List;

import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.InstanceRequirements;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.LaunchTemplateData;

import software.amazon.awssdk.services.ec2.model.AcceleratorCountRequest;
import software.amazon.awssdk.services.ec2.model.AcceleratorTotalMemoryMiBRequest;
import software.amazon.awssdk.services.ec2.model.ArchitectureType;
import software.amazon.awssdk.services.ec2.model.BaselineEbsBandwidthMbpsRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstanceAttributeRequest;
import software.amazon.awssdk.services.ec2.model.GetInstanceTypesFromInstanceRequirementsRequest;
import software.amazon.awssdk.services.ec2.model.InstanceAttributeName;
import software.amazon.awssdk.services.ec2.model.InstanceRequirementsRequest;
import software.amazon.awssdk.services.ec2.model.MemoryGiBPerVCpuRequest;
import software.amazon.awssdk.services.ec2.model.MemoryMiBRequest;
import software.amazon.awssdk.services.ec2.model.NetworkInterfaceCountRequest;
import software.amazon.awssdk.services.ec2.model.TotalLocalStorageGBRequest;
import software.amazon.awssdk.services.ec2.model.VCpuCountRangeRequest;
import software.amazon.awssdk.services.ec2.model.VirtualizationType;

/**
 * This class is a centralized placeholder for:
 * - API request construction, and
 * - object translation to/from the AWS SDK.
 */
public class Translator {

    /**
     * Build and return a DescribeInstanceAttributeRequest for
     * AWS::AutoScaling::LaunchConfiguration.
     *
     * @param targetInstanceId      String
     * @param instanceAttributeName InstanceAttributeName
     * @return DescribeInstanceAttributeRequest
     */
    public static DescribeInstanceAttributeRequest translateToDescribeInstanceAttributeRequest(
            final String targetInstanceId,
            final InstanceAttributeName instanceAttributeName) {
        return DescribeInstanceAttributeRequest
                .builder()
                .instanceId(targetInstanceId)
                .attribute(instanceAttributeName)
                .build();
    }

    /**
     * Build and return a GetInstanceTypesFromInstanceRequirementsRequest for
     * AWS::EC2::LaunchTemplate.
     *
     * @param launchTemplateData LaunchTemplateData
     * @param nextToken          String
     * @return GetInstanceTypesFromInstanceRequirementsRequest
     */
    public static GetInstanceTypesFromInstanceRequirementsRequest translateToGetInstanceTypesFromInstanceRequirementsRequest(
            final LaunchTemplateData launchTemplateData,
            final String nextToken) {
        final List<ArchitectureType> architectureTypes = new ArrayList<ArchitectureType>();
        architectureTypes.add(ArchitectureType.ARM64);
        architectureTypes.add(ArchitectureType.I386);
        architectureTypes.add(ArchitectureType.X86_64);
        architectureTypes.add(ArchitectureType.X86_64_MAC);

        final List<VirtualizationType> virtualizationTypes = new ArrayList<VirtualizationType>();
        virtualizationTypes.add(VirtualizationType.HVM);
        virtualizationTypes.add(VirtualizationType.PARAVIRTUAL);

        return GetInstanceTypesFromInstanceRequirementsRequest.builder()
                .architectureTypes(architectureTypes)
                .virtualizationTypes(virtualizationTypes)
                .instanceRequirements(
                        translateToGetInstanceRequirementsRequest(launchTemplateData.getInstanceRequirements()))
                .nextToken(nextToken)
                .build();
    }

    /**
     * Build and return an InstanceRequirementsRequest for AWS::EC2::LaunchTemplate.
     *
     * @param instanceRequirements InstanceRequirements
     * @return InstanceRequirementsRequest
     */
    public static InstanceRequirementsRequest translateToGetInstanceRequirementsRequest(
            final InstanceRequirements instanceRequirements) {
        InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder = InstanceRequirementsRequest
                .builder();

        instanceRequirementsRequestBuilder = translateFromVCpuCount(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromMemoryMiB(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromAcceleratorCount(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromAcceleratorManufacturers(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromAcceleratorNames(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromAcceleratorTotalMemoryMiB(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromAcceleratorTypes(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromBareMetal(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromBaselineEbsBandwidthMbps(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromBurstablePerformance(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromCpuManufacturers(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromExcludedInstanceTypes(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromInstanceGenerations(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromLocalStorage(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromLocalStorageTypes(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromMemoryGiBPerVCpu(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromNetworkInterfaceCount(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromOnDemandMaxPricePercentageOverLowestPrice(
                instanceRequirements, instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromRequireHibernateSupport(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromSpotMaxPricePercentageOverLowestPrice(instanceRequirements,
                instanceRequirementsRequestBuilder);

        instanceRequirementsRequestBuilder = translateFromTotalLocalStorageGBRequest(instanceRequirements,
                instanceRequirementsRequestBuilder);

        return instanceRequirementsRequestBuilder.build();
    }

    /**
     * Translate from VCpuCount and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromVCpuCount(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final VCpuCountRangeRequest.Builder vCpuCountRangeRequestBuilder = VCpuCountRangeRequest.builder();
        /*
         * When using InstanceRequirements, getVCpuCount() and getVCpuCount().getMin()
         * should not be null (the former is required, and the latter can be an integer
         * or zero to specify no minimum limit).
         */
        vCpuCountRangeRequestBuilder.min(instanceRequirements.getVCpuCount().getMin());
        if (instanceRequirements.getVCpuCount().getMax() != null)
            vCpuCountRangeRequestBuilder.max(instanceRequirements.getVCpuCount().getMax());
        instanceRequirementsRequestBuilder.vCpuCount(vCpuCountRangeRequestBuilder.build());
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from MemoryMiB and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromMemoryMiB(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final MemoryMiBRequest.Builder memoryMiBRequestBuilder = MemoryMiBRequest.builder();
        /*
         * When using InstanceRequirements, getMemoryMiB() and getMemoryMiB().getMin()
         * should not be null (the former is required, and the latter can be an integer
         * or zero to specify no minimum limit).
         */
        memoryMiBRequestBuilder.min(instanceRequirements.getMemoryMiB().getMin());
        if (instanceRequirements.getMemoryMiB().getMax() != null)
            memoryMiBRequestBuilder.max(instanceRequirements.getMemoryMiB().getMax());
        instanceRequirementsRequestBuilder.memoryMiB(memoryMiBRequestBuilder.build());
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from AcceleratorCount and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromAcceleratorCount(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final AcceleratorCountRequest.Builder acceleratorCountRequestBuilder = AcceleratorCountRequest.builder();
        if (instanceRequirements.getAcceleratorCount() != null) {
            if (instanceRequirements.getAcceleratorCount().getMin() != null)
                acceleratorCountRequestBuilder.min(instanceRequirements.getAcceleratorCount().getMin());
            if (instanceRequirements.getAcceleratorCount().getMax() != null)
                acceleratorCountRequestBuilder.max(instanceRequirements.getAcceleratorCount().getMax());
            instanceRequirementsRequestBuilder.acceleratorCount(acceleratorCountRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from AcceleratorManufacturers and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromAcceleratorManufacturers(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getAcceleratorManufacturers() != null)
            instanceRequirementsRequestBuilder
                    .acceleratorManufacturersWithStrings(instanceRequirements.getAcceleratorManufacturers()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from AcceleratorNames and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromAcceleratorNames(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getAcceleratorNames() != null)
            instanceRequirementsRequestBuilder
                    .acceleratorNamesWithStrings(instanceRequirements.getAcceleratorNames()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from AcceleratorTotalMemoryMiB and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromAcceleratorTotalMemoryMiB(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final AcceleratorTotalMemoryMiBRequest.Builder acceleratorTotalMemoryMiBRequestBuilder = AcceleratorTotalMemoryMiBRequest
                .builder();
        if (instanceRequirements.getAcceleratorTotalMemoryMiB() != null) {
            if (instanceRequirements.getAcceleratorTotalMemoryMiB().getMin() != null)
                acceleratorTotalMemoryMiBRequestBuilder
                        .min(instanceRequirements.getAcceleratorTotalMemoryMiB().getMin());
            if (instanceRequirements.getAcceleratorTotalMemoryMiB().getMax() != null)
                acceleratorTotalMemoryMiBRequestBuilder
                        .max(instanceRequirements.getAcceleratorTotalMemoryMiB().getMax());
            instanceRequirementsRequestBuilder
                    .acceleratorTotalMemoryMiB(acceleratorTotalMemoryMiBRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from AcceleratorTypes and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromAcceleratorTypes(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getAcceleratorTypes() != null)
            instanceRequirementsRequestBuilder
                    .acceleratorTypesWithStrings(instanceRequirements.getAcceleratorTypes()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from BareMetal and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromBareMetal(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getBareMetal() != null)
            instanceRequirementsRequestBuilder.bareMetal(instanceRequirements.getBareMetal()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from BaselineEbsBandwidthMbps and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromBaselineEbsBandwidthMbps(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final BaselineEbsBandwidthMbpsRequest.Builder baselineEbsBandwidthMbpsRequestBuilder = BaselineEbsBandwidthMbpsRequest
                .builder();
        if (instanceRequirements.getBaselineEbsBandwidthMbps() != null) {
            if (instanceRequirements.getBaselineEbsBandwidthMbps().getMin() != null)
                baselineEbsBandwidthMbpsRequestBuilder.min(instanceRequirements.getBaselineEbsBandwidthMbps().getMin());
            if (instanceRequirements.getBaselineEbsBandwidthMbps().getMax() != null)
                baselineEbsBandwidthMbpsRequestBuilder.max(instanceRequirements.getBaselineEbsBandwidthMbps().getMax());
            instanceRequirementsRequestBuilder.baselineEbsBandwidthMbps(baselineEbsBandwidthMbpsRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from BurstablePerformance and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromBurstablePerformance(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getBurstablePerformance() != null)
            instanceRequirementsRequestBuilder.burstablePerformance(instanceRequirements.getBurstablePerformance())
                    .build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from CpuManufacturers and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromCpuManufacturers(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getCpuManufacturers() != null)
            instanceRequirementsRequestBuilder
                    .cpuManufacturersWithStrings(instanceRequirements.getCpuManufacturers()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from ExcludedInstanceTypes and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromExcludedInstanceTypes(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getExcludedInstanceTypes() != null)
            instanceRequirementsRequestBuilder
                    .excludedInstanceTypes(instanceRequirements.getExcludedInstanceTypes()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from InstanceGenerations and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromInstanceGenerations(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getInstanceGenerations() != null)
            instanceRequirementsRequestBuilder
                    .instanceGenerationsWithStrings(instanceRequirements.getInstanceGenerations()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from LocalStorage and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromLocalStorage(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getLocalStorage() != null)
            instanceRequirementsRequestBuilder.localStorage(instanceRequirements.getLocalStorage()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from LocalStorageTypes and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromLocalStorageTypes(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getLocalStorageTypes() != null)
            instanceRequirementsRequestBuilder
                    .localStorageTypesWithStrings(instanceRequirements.getLocalStorageTypes()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from MemoryGiBPerVCpu and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromMemoryGiBPerVCpu(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final MemoryGiBPerVCpuRequest.Builder memoryGiBPerVCpuRequestBuilder = MemoryGiBPerVCpuRequest.builder();
        if (instanceRequirements.getMemoryGiBPerVCpu() != null) {
            if (instanceRequirements.getMemoryGiBPerVCpu().getMin() != null)
                memoryGiBPerVCpuRequestBuilder.min(instanceRequirements.getMemoryGiBPerVCpu().getMin());
            if (instanceRequirements.getMemoryGiBPerVCpu().getMax() != null)
                memoryGiBPerVCpuRequestBuilder.max(instanceRequirements.getMemoryGiBPerVCpu().getMax());
            instanceRequirementsRequestBuilder.memoryGiBPerVCpu(memoryGiBPerVCpuRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from NetworkInterfaceCount and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromNetworkInterfaceCount(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final NetworkInterfaceCountRequest.Builder networkInterfaceCountRequestBuilder = NetworkInterfaceCountRequest
                .builder();
        if (instanceRequirements.getNetworkInterfaceCount() != null) {
            if (instanceRequirements.getNetworkInterfaceCount().getMin() != null)
                networkInterfaceCountRequestBuilder.min(instanceRequirements.getNetworkInterfaceCount().getMin());
            if (instanceRequirements.getNetworkInterfaceCount().getMax() != null)
                networkInterfaceCountRequestBuilder.max(instanceRequirements.getNetworkInterfaceCount().getMax());
            instanceRequirementsRequestBuilder.networkInterfaceCount(networkInterfaceCountRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from OnDemandMaxPricePercentageOverLowestPrice and return the
     * updated InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromOnDemandMaxPricePercentageOverLowestPrice(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getOnDemandMaxPricePercentageOverLowestPrice() != null)
            instanceRequirementsRequestBuilder.onDemandMaxPricePercentageOverLowestPrice(
                    instanceRequirements.getOnDemandMaxPricePercentageOverLowestPrice()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from RequireHibernateSupport and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromRequireHibernateSupport(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getRequireHibernateSupport() != null)
            instanceRequirementsRequestBuilder
                    .requireHibernateSupport(instanceRequirements.getRequireHibernateSupport()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from SpotMaxPricePercentageOverLowestPrice and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromSpotMaxPricePercentageOverLowestPrice(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        if (instanceRequirements.getSpotMaxPricePercentageOverLowestPrice() != null)
            instanceRequirementsRequestBuilder.spotMaxPricePercentageOverLowestPrice(
                    instanceRequirements.getSpotMaxPricePercentageOverLowestPrice()).build();
        return instanceRequirementsRequestBuilder;
    }

    /**
     * Translate from TotalLocalStorageGBRequest and return the updated
     * InstanceRequirementsRequest.Builder.
     *
     * @param instanceRequirements               InstanceRequirements
     * @param instanceRequirementsRequestBuilder InstanceRequirementsRequest.Builder
     * @return InstanceRequirementsRequest.Builder
     */
    private static InstanceRequirementsRequest.Builder translateFromTotalLocalStorageGBRequest(
            final InstanceRequirements instanceRequirements,
            final InstanceRequirementsRequest.Builder instanceRequirementsRequestBuilder) {
        final TotalLocalStorageGBRequest.Builder totalLocalStorageGBRequestBuilder = TotalLocalStorageGBRequest
                .builder();
        if (instanceRequirements.getTotalLocalStorageGB() != null) {
            if (instanceRequirements.getTotalLocalStorageGB().getMin() != null)
                totalLocalStorageGBRequestBuilder.min(instanceRequirements.getTotalLocalStorageGB().getMin());
            if (instanceRequirements.getTotalLocalStorageGB().getMax() != null)
                totalLocalStorageGBRequestBuilder.max(instanceRequirements.getTotalLocalStorageGB().getMax());
            instanceRequirementsRequestBuilder.totalLocalStorageGB(totalLocalStorageGBRequestBuilder.build());
        }
        return instanceRequirementsRequestBuilder;
    }

}
