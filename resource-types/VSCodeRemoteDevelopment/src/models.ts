// This is a generated file. Modifications will be overwritten.
import { BaseModel, Dict, integer, Integer, Optional, transformValue } from 'cfn-rpdk';
import { Exclude, Expose, Type, Transform } from 'class-transformer';

export class ResourceModel extends BaseModel {
    ['constructor']: typeof ResourceModel;

    @Exclude()
    public static readonly TYPE_NAME: string = 'AWSSamples::Devtools::Devinstance';

    @Exclude()
    protected readonly IDENTIFIER_KEY_UID: string = '/properties/UID';

    @Expose({ name: 'UID' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'uID', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    uID?: Optional<string>;
    @Expose({ name: 'InstanceType' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'instanceType', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    instanceType?: Optional<string>;
    @Expose({ name: 'DiskSize' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(Integer, 'diskSize', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    diskSize?: Optional<integer>;
    @Expose({ name: 'Keypair' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'keypair', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    keypair?: Optional<string>;
    @Expose({ name: 'SSH' })
    @Transform(
        (value: any, obj: any) =>
            transformValue(String, 'sSH', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    sSH?: Optional<string>;

    @Exclude()
    public getPrimaryIdentifier(): Dict {
        const identifier: Dict = {};
        if (this.uID != null) {
            identifier[this.IDENTIFIER_KEY_UID] = this.uID;
        }

        // only return the identifier if it can be used, i.e. if all components are present
        return Object.keys(identifier).length === 1 ? identifier : null;
    }

    @Exclude()
    public getAdditionalIdentifiers(): Array<Dict> {
        const identifiers: Array<Dict> = new Array<Dict>();
        // only return the identifiers if any can be used
        return identifiers.length === 0 ? null : identifiers;
    }
}

